from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    tools=[google_search]
)
