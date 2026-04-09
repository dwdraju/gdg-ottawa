# Setup and Preparation

This guide covers the preparation and setup for building AI agents using `uv` and `google-adk`.

## Preparation

### Install uv
First, ensure you have `uv` installed. You can install it using the following command:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
For more information, see the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### Create a Project Folder
Create a new directory for your project and navigate into it:
```bash
mkdir learn-ai-agents
cd learn-ai-agents
```

## Project Initialization

1. **Initialize the project:**
   ```bash
   uv init
   ```

2. **Verify the initialization:**
   ```bash
   ls
   ```

3. **Add Google ADK:**
   ```bash
   uv add google-adk
   uv add a2a-sdk
   ```

4. **Verify the addition:**
   ```bash
   cat pyproject.toml
   ```

## Create Your First Agent

Create a new agent named `myfirstagent`:
```bash
mkdir agents
uv run adk create agents/firstagent
```

**During the creation process, select the following options:**

1. **Choose a model for the root agent:**
   
   Select `1. gemini-2.5-flash` (or the latest version mentioned).
   *User prompt selection: `1`*

3. **Select Provider:**
   
   Select `1. Google AI`.

   > [!IMPORTANT]
   > When you select **Google AI**, you will be asked for an API Key.
   > - If you don't have one, create it in **AI Studio**: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey).
   > - Generating an API key in AI Studio **does not require a billing account**.

## Run the Agent

1. **Start the web interface:**
   ```bash
   uv run adk web agents --port 8000
   ```

2. **Interact with the agent:**
   
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Google Search Tools
1. **Import google search tools in in `agents/firstagent/agent.py`**
```
from google.adk.tools import google_search
```

2. **Update `root_agent` definition in `agents/firstagent/agent.py` to include google search tools**
```
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[google_search]
)
```
3. **Restart the web interface and interact with agent**
   ```bash
   uv run adk web agents --port 8000
   ```
   Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).
