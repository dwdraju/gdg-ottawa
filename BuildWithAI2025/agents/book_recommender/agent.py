from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="book_recommender",
    model="gemini-2.0-flash",
    description="Agent that recommends books based on your preferences.",
    instruction=(
        "Your goal is to recommend a book based on the user's genre and mood preferences.\n"
        "1. Ask the user for their preferred genre and mood if they haven't provided them.\n"
        "2. Use the `google_search` tool to find a recommendation based on the user's genre and mood.\n"
        "4. Present the final recommendation to the user."
    ),
    tools=[google_search]
)
