# MCP Server

This project contains a demo MCP server to run on Cloud Run environment.

For deployment instructions, please refer to this codelab:
https://codelabs.developers.google.com/codelabs/cloud-run/how-to-deploy-a-secure-mcp-server-on-cloud-run


### Deploy to Cloud Run
```
gcloud run deploy zoo-mcp-server \
	--no-allow-unauthenticated \
	--region=us-central1 \
	--source=. \
	--labels=dev-tutorial=codelab-mcp
```

### Get token for Gemini CLI to access MCP Server
```
export ID_TOKEN=$(gcloud auth print-identity-token)
```


### Cleanup deployment
```
gcloud run services delete zoo-mcp-server
```
