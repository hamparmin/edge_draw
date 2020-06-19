"""Programatically interact with a Google Cloud Storage bucket."""
from os import listdir
from os.path import isfile, join
from random import randint
from google.cloud import storage


def upload_files(bucketName,file):
    """Upload files to GCP bucket."""
    files = [f for f in listdir(localFolder) if isfile(join(localFolder, f))]
    for file in files:
        localFile = localFolder + file
        blob = bucket.blob(bucketFolder + file)
        blob.upload_from_filename(localFile)
    return f'Uploaded {files} to "{bucketName}" bucket.'


def list_files(bucketName):
    """List all files in GCP bucket."""
    files = bucket.list_blobs(prefix=bucketFolder)
    fileList = [file.name for file in files if '.' in file.name]
    return fileList


def download_random_file(bucketName, bucketFolder, localFolder):
    """Download random file from GCP bucket."""
    fileList = list_files(bucketName)
    rand = randint(0, len(fileList) - 1)
    blob = bucket.blob(fileList[rand])
    fileName = blob.name.split('/')[-1]
    blob.download_to_filename(localFolder + fileName)
    return f'{fileName} downloaded from bucket.'


def delete_file(bucketName, bucketFolder, fileName):
    """Delete file from GCP bucket."""
    bucket.delete_blob(bucketFolder + fileName)
    return f'{fileName} deleted from bucket.'


def rename_file(bucketName, bucketFolder, fileName, newFileName):
    """Rename file in GCP bucket."""
    blob = bucket.blob(bucketFolder + fileName)
    bucket.rename_blob(blob,
                       new_name=newFileName)
    return f'{fileName} renamed to {newFileName}.'
