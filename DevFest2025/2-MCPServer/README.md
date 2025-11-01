# MCP Server

This project contains a demo MCP server.

For deployment instructions, please refer to this codelab:
https://codelabs.developers.google.com/codelabs/cloud-run/how-to-deploy-a-secure-mcp-server-on-cloud-run

```
gcloud run deploy zoo-mcp-server \
	--no-allow-unauthenticated \
	--region=us-central1 \
	--source=. \
	--labels=dev-tutorial=codelab-mcp
```

Clean deployment
```
gcloud run services delete zoo-mcp-server
```
