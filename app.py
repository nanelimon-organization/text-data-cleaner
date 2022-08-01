from flask import Flask, render_template


app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = ['.xlsx']
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


@app.errorhandler(413)
def too_large(e):
    return "Dosya boyutu 1GB tan fazla!", 413


@app.route('/')
def index():
    return render_template('index.html')