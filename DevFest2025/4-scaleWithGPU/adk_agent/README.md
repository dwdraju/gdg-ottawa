# Production Agent with GPU

This project demonstrates how to deploy a production-ready agent that leverages GPU for accelerated performance. The agent is built to be scalable and resilient, suitable for real-world applications.

## Getting Started

To get started with this project, you'll need to have the following prerequisites installed:

*   [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
*   [Python 3.10+](https://www.python.org/downloads/)
*   [uv](https://github.com/astral-sh/uv)
*   [Docker](https://docs.docker.com/get-docker/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/dwdraju/gdg-ottawa.git
    cd DevFest2025/3-scaleWithGPU/adk_agent
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    uv venv
    uv pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**

    Create a `.env` file by copying the example file:

    ```bash
    cp .env.example .env
    ```

    Then, edit the `.env` file with your specific configuration.

## Deployment

To deploy the agent to Google Cloud Run, you can use the following command. This command will build and deploy the agent, setting the necessary environment variables and configurations.

```bash
export PROJECT_ID=$(gcloud config get-value project)
export OLLAMA_URL=https://ollama-gemma3-270m-gpu-757935627251.europe-west1.run.app
export AGENT_URL=https://production-adk-agent-757935627251.europe-west1.run.app

gcloud run deploy production-adk-agent \
   --source . \
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
uv run locust -f load-test.py \
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
