# DevFest Ottawa 2025 — Node.js preview server

This small Node.js app serves the static `index.html` and assets so you can preview the DevFest Ottawa site locally.

Quick start

1. From the `website` folder, install dependencies:

```bash
npm install
```

2. Start the server:

```bash
npm start
```

3. Open http://localhost:8080 in your browser.

Development

Run with automatic reload (requires `nodemon`):

```bash
npm run dev
```

Notes

- The server serves static files from the same folder as `server.js`.
- Change `PORT` with `PORT=8080 npm start` to run on a different port.

4. Deploy to Cloud Run(~3 Minutes)
```bash
gcloud run deploy gdg-devfest-ottawa --source . \
	--concurrency 10 \
	--min 1 \
	--max 5 \
	--allow-unauthenticated
```

5. Cleanup deployment
```bash
gcloud run services delete gdg-devfest-ottawa
```
