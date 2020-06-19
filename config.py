"""Google Cloud Storage Configuration."""
from os import environ

# Google Cloud Storage
bucketName = environ.get('edge-detect-project.appspot.com')
bucketFolder = environ.get('uploads')

# Data
localFolder = environ.get("localFolder/")

#set credentials
credential_path = "credentials.json"
environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path