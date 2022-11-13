from flask import Flask, request
from flask_cors import CORS
from google.cloud import storage, vision
import time
import math
import base64

app = Flask(__name__)
CORS(app)

d = {
  "status": 200,
  "name": "the correct image"
}

@app.route("/")
def hello_world():
  return d
  
@app.route("/images", methods = ['GET', 'POST'])
def post_image():
  name = request.form.get("name")
  img = request.form.get("file_attachment")
  img = img.replace('data:image/png;base64,', '')
  decoded_img = base64.b64decode(img)
  d = {
    "status": 200,
    "name": name
  }
  current_time = str(math.floor(time.time()))
  upload_blob_from_memory("photo-captures", decoded_img, '{}.png'.format(current_time))
  return d

def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The contents to upload to the file
    # contents = "these are my contents"

    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"{destination_blob_name} uploaded to {bucket_name}."
    )