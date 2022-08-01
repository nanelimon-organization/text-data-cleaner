import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, abort
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


@app.errorhandler(413)
def too_large(e):
    return "Dosya boyutu 1GB tan fazla!", 413


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    my_files = request.files
    formData = request.form['myFormData']

    with open("my_data.txt", "w+") as my_data:
        my_data.write(formData)

    for item in my_files:
        uploaded_file = my_files.get(item)
        uploaded_file.filename = secure_filename(uploaded_file.filename)

        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

        uploaded_file.save(uploaded_file.filename)

    return redirect(url_for('index'))


@app.route('/data_cleaning')
def data_cleaning():
    try:
        df = pd.read_excel('data.xlsx')
        cleaning(df)
    except Exception as e:
        print('Alınan data temizlenirken bir hata oluştu', e)
    else:
        return redirect(url_for('index'))


def cleaning(df):
    print('temizleme işleri')
    print(df.head())