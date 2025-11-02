# Prototype to Production - Deploy Your ADK Agent to Cloud Run with GPU

This project demonstrates how to deploy a production-ready agent that leverages GPU for accelerated performance. The agent is built to be scalable and resilient, suitable for real-world applications.

This project is based on the Google Codelab: [Prototype to Production - Deploy Your ADK Agent to Cloud Run with GPU](https://codelabs.developers.google.com/codelabs/cloud-run/how-to-connect-adk-to-deployed-cloud-run-llm#0)

## Project Structure

*   `adk_agent/`: Contains the production-ready agent, including the Dockerfile for deployment and a load testing script.
*   `ollama/`: Contains the configuration for deploying the Ollama Gemma3 model on Google Cloud Run with GPU acceleration.

## Getting Started

To get started with this project, you'll need to have the following prerequisites installed:

*   [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
*   [Python 3.10+](https://www.python.org/downloads/)
*   [uv](https://github.com/astral-sh/uv)
*   [Docker](https://docs.docker.com/get-docker/)

## Deployment

The deployment process involves two main steps: deploying the Ollama model and then deploying the agent.

### 1. Deploying Ollama with Gemma3 on Google Cloud Run

The following command deploys the Ollama Gemma3 model as a Cloud Run service with GPU acceleration.

```bash
gcloud run deploy ollama-gemma3-270m-gpu \
  --source ./ollama \
  --region europe-west1 \
  --concurrency 7 \
  --cpu 8 \
  --set-env-vars OLLAMA_NUM_PARALLEL=4 \
  --gpu 1 \
  --gpu-type nvidia-l4 \
  --max-instances 3 \
  --memory 16Gi \
  --allow-unauthenticated \
  --no-cpu-throttling \
  --no-gpu-zonal-redundancy \
  --timeout 600 \
  --labels dev-tutorial=codelab-agent-gpu
```

After deployment, get the URL of the Ollama service:

```bash
export OLLAMA_URL=$(gcloud run services describe ollama-gemma3-270m-gpu \
    --region=europe-west1 \
    --format="value(status.url)")

echo "🎉 Gemma backend deployed at: $OLLAMA_URL"
```

### 2. Deploying the Production Agent

To deploy the agent to Google Cloud Run, you can use the following command. This command will build and deploy the agent, setting the necessary environment variables and configurations.

```bash
export PROJECT_ID=$(gcloud config get-value project)
export AGENT_URL=https://production-adk-agent-757935627251.europe-west1.run.app

gcloud run deploy production-adk-agent \
   --source ./adk_agent \
   --region europe-west1 \
   --allow-unauthenticated \
   --memory 4Gi \
   --cpu 2 \
   --max-instances 1 \
   --concurrency 50 \
   --timeout 300 \
   --set-env-vars GOOGLE_CLOUD_PROJECT=$PROJECT_ID \
   --set-env-vars GOOGLE_CLOUD_LOCATION=europe-west1 \
   --set-env-vars GEMMA_MODEL_NAME=gemma3:270m \
   --set-env-vars OLLAMA_API_BASE=$OLLAMA_URL \
   --labels dev-tutorial=codelab-agent-gpu
```

## Load Testing

You can perform a load test on the deployed agent using the following command. This will simulate 20 concurrent users for 60 seconds, with a spawn rate of 5 users per second.

```bash
uv run locust -f adk_agent/load-test.py \
   -H $AGENT_URL \
   --headless \
   -t 60s \
   -u 20 \
   -r 5
```

**Load Test Parameters:**

*   **Duration:** 60 seconds
*   **Users:** 20 concurrent users
*   **Spawn rate:** 5 users per second

## Resources

*   **Official Ollama Documentation:** [https://ollama.com/](https://ollama.com/)
*   **Google Cloud Run Documentation:** [https://cloud.google.com/run/docs](https://cloud.google.com/run/docs)
