from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import requests

def get_country_info(country_name: str) -> str:
    """Fetch capital, region, and population of the given country."""
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()[0]
        capital = data.get("capital", ["Unknown"])[0]
        region = data.get("region", "Unknown")
        population = data.get("population", "Unknown")

        return f"{country_name} is in {region}. Capital: {capital}. Population: {population}."
    except Exception as e:
        return f"Could not retrieve data for {country_name}. Error: {e}"

greeting_agent = Agent(
    model='gemini-2.5-flash-lite',
    name="greeting_agent",
    instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. " "Do not engage in any other conversation or tasks.",
    description="Handles simple greetings and hellos",
 )

farewell_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o-mini"),
    name="farewell_agent",
    instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. Do not perform any other actions.",
    description="Handles simple farewells and goodbyes",        
 )

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that can fetch basic information about countries using a public API.',
    instruction='Ask me about a country to get its capital, region, and population.',
    tools=[get_country_info],
    sub_agents=[greeting_agent,farewell_agent]
)
