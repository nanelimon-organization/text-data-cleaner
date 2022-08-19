import re
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, abort, send_file
import os
from werkzeug.utils import secure_filename
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
app.config['MAX_CONTENT_LENGTH'] = 2048 * 2048

app.config.update(
    UPLOADED_PATH=os.path.join(dir_path, 'static/'),
    DROPZONE_MAX_FILES=1,
    DROPZONE_DEFAULT_MESSAGE='Dosyaları yüklemek için buraya bırakınız..'
)


def turkish_char(text):
    translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    result = text.translate(translationTable)
    return result


def cleaning(text):
    text = str(text).lower()
    text = " ".join([word for word in text.split() if '#' not in word and '@' not in word])
    text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    text = re.sub(r'''      
                   \W+       # Bir veya daha fazla sözcük olmayan karakter
                   \s*       # artı sıfır veya daha fazla boşluk karakteri,
                   ''',
                  ' ',
                  text,
                  flags=re.VERBOSE)
    text = re.sub("\d+", "", text)
    return text


@app.errorhandler(413)
def too_large(e):
    return "Dosya boyutu 1GB tan fazla!", e, 413


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    my_files = request.files
    formData = request.form['myFormData']

    with open("static/my_data.txt", "w+") as my_data:
        my_data.write(formData)

    for item in my_files:
        uploaded_file = my_files.get(item)
        uploaded_file.filename = secure_filename(uploaded_file.filename)

        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        try:
            uploaded_file.save(os.path.join(app.config['UPLOADED_PATH'] + 'data.xlsx'))
        except Exception as e:
            print(f'Hata! {e}\n Veriseti .xlsx formatında değil!')

    return redirect(url_for('index'))


@app.route('/data_cleaning')
def data_cleaning():
    try:
        df = pd.read_excel(f"static/data.xlsx")
        textList = df.text.apply(turkish_char)
        textList = textList.apply(cleaning)
        textList = list(textList)
        df['clean_data'] = textList
        df.to_csv('static/clean_data.csv', index=False)
    except Exception as e:
        print('Alınan data temizlenirken bir hata oluştu', e)
    else:
        return send_file('static/clean_data.csv', as_attachment=True)
