from flask import Flask
from werkzeug import exceptions

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.errorhandler(exceptions.BadRequest)
def handle_bad_request(e):
    return str(e), 400


@app.errorhandler(Exception)
def handle_bad_request(e):
    return str(e), 500
