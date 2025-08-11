# BuildWithAI2025 Agents

This repository contains a collection of agents built with Gemini.

## Agents

*   [Book Recommender](./agents/book_recommender)
*   [Country Info Agent](./agents/country-info-agent)
*   [My Agent](./agents/my-agent)

---

## Environment Variables

Before deploying the agents, you need to set up the required environment variables. Each agent has a `.env.example` file that lists the necessary variables. Copy the `.env.example` file to a `.env` file and fill in the values.

For example, for the `country-info-agent`:

```bash
cp agents/country-info-agent/.env.example agents/country-info-agent/.env
```

Then, edit the `agents/country-info-agent/.env` file and add the required values.

Make sure you have set the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` environment variables in your shell. These variables are used in the deployment commands.

---

## Deployment

Below are the deployment instructions for each agent.

### Book Recommender Agent

#### Deploy to Cloud Run

```bash
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name="book-recommender-agent" \
--app_name="book-recommender-agent" \
--with_ui \
./agents/book_recommender
```

#### Deploy to Agent Engine

```bash
adk deploy agent_engine \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --staging_bucket gs://$GOOGLE_CLOUD_PROJECT-agent \
  --display_name "book-recommender-agent" \
  --trace_to_cloud \
  ./agents/book_recommender
```

---

### Country Info Agent

#### Deploy to Cloud Run

```bash
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name="country-info-agent" \
--app_name="country-info-agent" \
--with_ui \
./agents/country-info-agent
```

#### Deploy to Agent Engine

```bash
adk deploy agent_engine \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --staging_bucket gs://$GOOGLE_CLOUD_PROJECT-agent \
  --display_name "country-info-agent" \
  --trace_to_cloud \
  ./agents/country-info-agent
```

---

### My Agent

#### Deploy to Cloud Run

```bash
adk deploy cloud_run \
--project=$GOOGLE_CLOUD_PROJECT \
--region=$GOOGLE_CLOUD_LOCATION \
--service_name="my-agent" \
--app_name="my-agent" \
--with_ui \
./agents/my-agent
```

#### Deploy to Agent Engine

```bash
adk deploy agent_engine \
  --project=$GOOGLE_CLOUD_PROJECT \
  --region=$GOOGLE_CLOUD_LOCATION \
  --staging_bucket gs://$GOOGLE_CLOUD_PROJECT-agent \
  --display_name "my-agent" \
  --trace_to_cloud \
  ./agents/my-agent
```