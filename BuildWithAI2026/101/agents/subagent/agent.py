from google.adk.agents.llm_agent import Agent

prime_agent = Agent(
    model='gemini-2.5-flash',
    name="prime_agent",
    description="A specialized agent for primality testing. It determines whether a given integer is a prime number.",
    instruction="Analyze the provided number and determine if it is prime. Respond with a clear statement of whether the number is prime or composite.",
)

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="A general-purpose assistant that handles various user queries and coordinates specialized tasks with sub-agents.",
    instruction="Act as the primary interface for the user. Answer general questions directly. For any inquiries regarding prime numbers, delegate the check to the 'prime_agent' and provide the final result to the user.",
    sub_agents=[prime_agent],
)
