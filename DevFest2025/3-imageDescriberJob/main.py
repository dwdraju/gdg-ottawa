import os
from google.cloud import storage
from vertexai.preview.generative_models import GenerativeModel, Part
from vertexai.preview.generative_models import Image
import vertexai

PROJECT_ID = os.environ.get("PROJECT_ID", "gkerocks")
REGION = os.environ.get("REGION", "us-central1")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "ottawa-devfest-images")
IMAGE_PATH_PREFIX = os.environ.get("IMAGE_PATH_PREFIX", "")  # e.g. "images/"
OUTPUT_FILE = "output.txt"

def list_jpg_images(bucket_name, prefix=""):
    """List all JPG/JPEG images in the GCS bucket under the given prefix."""
    client = storage.Client()
    blobs = client.list_blobs(bucket_name, prefix=prefix)
    image_blobs = [b.name for b in blobs if b.name.lower().endswith((".jpg", ".jpeg"))]
    print(f"Found {len(image_blobs)} images in gs://{bucket_name}/{prefix}")
    return image_blobs

def download_image(bucket_name, blob_name, local_path):
    """Download image from GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(local_path)
    return local_path

def upload_to_gcs(bucket_name, local_path, dest_blob_name):
    """Upload local file to GCS."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob_name)
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{bucket_name}/{dest_blob_name}")

def describe_image(model, image_path):
    """Generate description for an image using Vertex AI Gemini."""
    with open(image_path, "rb") as f:
        image_part = Part.from_data(mime_type="image/jpeg", data=f.read())
    prompt = "Describe this image in detail for a report."
    response = model.generate_content([prompt, image_part])
    return response.text.strip()

def main():
    vertexai.init(project=PROJECT_ID, location=REGION)
    model = GenerativeModel("gemini-2.5-flash-image")

    image_blobs = list_jpg_images(BUCKET_NAME, IMAGE_PATH_PREFIX)
    if not image_blobs:
        print("No images found.")
        return

    with open(OUTPUT_FILE, "w") as out:
        for blob_name in image_blobs:
            local_filename = os.path.basename(blob_name)
            download_image(BUCKET_NAME, blob_name, local_filename)
            print(f"Processing {blob_name}...")
            try:
                description = describe_image(model, local_filename)
                out.write(f"Image: {blob_name}\n")
                out.write(f"Description: {description}\n\n")
                print(f"Done describing {blob_name}")
            except Exception as e:
                print(f"Error processing {blob_name}: {e}")
    
    upload_to_gcs(BUCKET_NAME, OUTPUT_FILE, f"{IMAGE_PATH_PREFIX.rstrip('/')}output.txt")
    print("All image descriptions written to output.txt and uploaded to GCS.")

if __name__ == "__main__":
    main()
