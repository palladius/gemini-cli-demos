from google.adk.agents import Agent
from google.adk.tools import FunctionTool

def fancy_hello() -> str:
  """Returns a fancy greeting string."""
  return "Hello from your friendly ADK Agent! 🚀"

root_agent = Agent(
    name="hello_agent",
    model="gemini-2.5-flash",
    instruction="You have one job: greet the user by calling the fancy_hello tool.",
    description="A simple agent that provides a fancy greeting.",
    tools=[FunctionTool(fancy_hello)],
)
