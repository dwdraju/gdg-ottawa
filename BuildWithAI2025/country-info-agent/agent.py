from google.adk.agents import Agent
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

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that can fetch basic information about countries using a public API.',
    instruction='Ask me about a country to get its capital, region, and population.',
    tools=[get_country_info],
)
