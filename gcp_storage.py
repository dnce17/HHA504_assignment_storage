from google.cloud import storage
from PIL import Image
import io
import os

# Step 1: Set up your Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_secret.json' # Change this to your key file name

# Step 2: Create a Google Cloud Storage client
client = storage.Client()

# Step 3: Create a bucket or use an existing one
bucket_name = 'test-bucket-for-learning-use'  # Change this to your bucket name
bucket = client.bucket(bucket_name)

# Uploading outside images
# Create a list of files in /images with path 
files_upload = []
for root, dirs, files in os.walk("img/xrays"):  # Change this to the path where imgs are stored
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    ## print working on
    print(f"Working on {file}")
    ## load file using io into memory
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    print(file)
    ## Just keep file name 
    file = file.split("/")[-1]
    print('New file name:', file)
    # Upload file to GCS
    try:
        blob = bucket.blob(file)
        blob.upload_from_string(file_byte_array, content_type='image/png')
        print(f"Outside image uploaded successfully to Google Cloud Storage!")
    except Exception as e:
        print(f"Error: {e}")

# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')

# Step 5: Upload the fake image to Google Cloud Storage
blob = bucket.blob('fake_image.png')    # Change to desired name for this fake img
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')  # Change to ensure sure extension matches

print("Fake image uploaded successfully to Google Cloud Storage!")