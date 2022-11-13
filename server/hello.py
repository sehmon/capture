from flask import Flask, request
from flask_cors import CORS
from google.cloud import storage, vision, firestore
import time
import math
import base64

config = {
  "apiKey": "AIzaSyDo7QrSzXvWbIPb8XLs8qnCCy4EA9cEmd4",
  "authDomain": "capture-368502.firebaseapp.com",
  "projectId": "capture-368502",
  "storageBucket": "capture-368502.appspot.com",
  "messagingSenderId": "728673045298",
  "appId": "1:728673045298:web:92440ad29f3b3e76b4e52b",
  "measurementId": "G-QQ6RPGDZQY"
}

db = firestore.Client(project="capture-368502")

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
  return "Hello World"
  
@app.route("/images", methods = ['GET', 'POST'])
def post_image():
  current_time = str(math.floor(time.time()))
  photo_upload_name = '{}.png'.format(current_time)
  img_url = 'https://storage.googleapis.com/photo-captures/{}'.format(photo_upload_name)

  name = request.form.get("name")
  img = request.form.get("file_attachment")
  img = img.replace('data:image/png;base64,', '')
  decoded_img = base64.b64decode(img)
  d = {
    "status": 200,
    "name": name
  }
  current_time = str(math.floor(time.time()))
  upload_blob_from_memory("photo-captures", decoded_img, photo_upload_name)
  img_properties = run_object_detection(photo_upload_name)
  doc_ref = db.collection('photos').document(photo_upload_name)
  doc_ref.set({
    'properties': 'test properties!!!!',
    'img_url': img_url
  })
  return {"status": 200, "details": "It's all good"}

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
  
def run_object_detection(cloud_photo_name):
  """ Runs cloud vision object detection API on file """
  cloud_image_uri = 'gs://photo-captures/{}'.format(cloud_photo_name)
  vision_client = vision.ImageAnnotatorClient()
  response = vision_client.annotate_image({
    'image': {'source': {'image_uri': cloud_image_uri}},
    'features': [
      {'type_': vision.Feature.Type.IMAGE_PROPERTIES},
      {'type_': vision.Feature.Type.OBJECT_LOCALIZATION}
      ]
  })
  return response