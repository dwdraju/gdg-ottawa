# Vertex AI Image Describer

## Table of Contents

*   [Description](#description)
*   [Prerequisites](#prerequisites)
*   [Configuration](#configuration)
*   [How to Run](#how-to-run)

This project uses the Vertex AI Gemini Flash Image model to generate descriptions for images stored in a Google Cloud Storage bucket.

## Description

The script `main.py` performs the following steps:

1.  Lists all JPG/JPEG images in a specified Google Cloud Storage bucket.
2.  Downloads each image locally.
3.  Uses the Vertex AI Gemini Flash Image model to generate a description for each image.
4.  Saves the descriptions to a local file named `output.txt`.
5.  Uploads the `output.txt` file back to the Google Cloud Storage bucket.

## Prerequisites

Before running this project, you need to have the following:

*   A Google Cloud Platform project.
*   The `gcloud` CLI installed and configured.
*   A Google Cloud Storage bucket with images.
*   An Artifact Registry repository to store the Docker image.

## Configuration

The following environment variables can be set to configure the `main.py` script:

| Variable            | Description                                                                 | Default Value          |
| ------------------- | --------------------------------------------------------------------------- | ---------------------- |
| `PROJECT_ID`        | Your Google Cloud project ID.                                               | `gkerocks`             |
| `REGION`            | The Google Cloud region.                                                    | `us-central1`          |
| `BUCKET_NAME`       | The name of your Google Cloud Storage bucket.                               | `ottawa-devfest-images` |
| `IMAGE_PATH_PREFIX` | (Optional) The prefix for the images in the bucket (e.g., `images/`).       | `""`                   |
| `OUTPUT_FILE`       | The name of the output file.                                                | `output.txt`           |

## How to Run

This section outlines the steps to build, deploy, and execute the image describer on Google Cloud Run.

### 1. Set Environment Variables

First, set the necessary environment variables. Replace `your-bucket-name` with the actual name of your Google Cloud Storage bucket.

```bash
REGION="us-central1"
PROJECT_ID=$(gcloud config get-value project)
NAME="image-describer"
BUCKET_NAME="ottawa-devfest-images" # Replace with your bucket name
```

### 2. Create Artifact Registry Repository

Create a Docker repository in Artifact Registry to store your Docker image.

```bash
gcloud artifacts repositories create $NAME-repo \
  --repository-format=docker \
  --location=$REGION \
  --description="Repository for Vertex AI image describer Cloud Run job"
```

### 3. Build and Push Docker Image

Build the Docker image and push it to the Artifact Registry using Cloud Build.

```bash
IMAGE=${REGION}-docker.pkg.dev/${PROJECT_ID}/$NAME-repo/${NAME}:latest
gcloud builds submit --tag $IMAGE
```

### 4. Create Cloud Run Job

Create a Cloud Run job using the Docker image you just pushed.

```bash
gcloud run jobs create ${NAME}-job \
  --image $IMAGE \
  --region=$REGION \
  --set-env-vars PROJECT_ID=$PROJECT_ID,BUCKET_NAME=$BUCKET_NAME
```

### 5. Execute Cloud Run Job

Finally, execute the Cloud Run job.

```bash
gcloud run jobs execute ${NAME}-job
```

### 6. Cleanup
```bash
gcloud artifacts repositories delete $NAME-repo --location=$REGION
gcloud run jobs delete $NAME-job

```
