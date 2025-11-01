# Deploying Ollama with Gemma3 on Google Cloud Run

This guide provides a streamlined approach to deploying the Ollama Gemma3 model on Google Cloud Run, leveraging the power of GPUs for accelerated performance.

## Deployment Steps (5 minutes)

The following command deploys the Ollama Gemma3 model as a Cloud Run service with GPU acceleration.

```bash
gcloud run deploy ollama-gemma3-270m-gpu \
  --source . \
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

## Resources

* **Official Ollama Documentation:** [https://ollama.com/](https://ollama.com/)
* **Google Cloud Run Documentation:** [https://cloud.google.com/run/docs](https://cloud.google.com/run/docs)
