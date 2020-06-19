from storage import *
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import testcv
from os import environ

# Google Cloud Storage
bucketName = 'edge-detect-project.appspot.com'
bucketFolder = 'uploads'

#set credentials
credential_path = "credentials.json"
environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = bucketFolder
app.config['ALLOWED_EXTENSIONS'] = set([ 'png', 'jpg', 'jpeg', 'JPG'])

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucketName)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print (filename)
        testcv.image_make(filename)
        return redirect(url_for('uploaded_file',
                                filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
    )
