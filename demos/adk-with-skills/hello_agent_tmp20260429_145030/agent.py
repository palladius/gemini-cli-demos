# Copyright 2026 Google LLC
from google.adk.agents import Agent
from google.adk.apps.app import App

root_agent = Agent(
    name="hello_agent",
    model="gemini-1.5-flash-002",
    instruction="You are a simple hello world agent. Just say hello back to the user.",
)

app = App(
    name="hello_agent",
    root_agent=root_agent,
)
