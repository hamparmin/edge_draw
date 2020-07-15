from storage import *
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from os import environ
import requests

# Google Cloud Storage
bucketName = 'mvp_images'
bucketFolder = 'uploads/'

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
        #upload file to a blob
        filename = secure_filename(file.filename)
        blob = bucket.blob(bucketFolder + filename)
        blob.upload_from_file(file)
        src=blob.public_url
        
  
    #render image in painter.html
    return render_template("painter.html", image_source=src)



if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=int("5000"),
        debug=True
    )
