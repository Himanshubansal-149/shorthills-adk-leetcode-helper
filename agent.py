from google.adk.agents import Agent, SequentialAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool, google_search 
import os

def get_dsa_template(topic: str) -> str:
    return f"#include <iostream>\n// Template for {topic}\nint main() {{ return 0; }}"

def complexity_analyzer(constraints: str) -> str:
    return "O(N log N) recommended"

def save_report(content: str) -> str:
    with open("contest_report.md", "w") as f:
        f.write(str(content))
    return "Report saved successfully."

scout = Agent(
    name="Scout",
    model="gemini-1.5-flash",
    instruction="Search for the latest LeetCode Weekly Contest problems.",
    tools=[google_search]
)

analyst = Agent(
    name="Analyst",
    model="gemini-1.5-flash",
    instruction="Identify the DSA patterns for these problems.",
    tools=[FunctionTool(complexity_analyzer)]
)

coder = Agent(
    name="Coder",
    model="gemini-1.5-flash",
    instruction="Write C++ templates and save the report.",
    tools=[FunctionTool(get_dsa_template), FunctionTool(save_report)]
)

root_agent = SequentialAgent(
    name="LeetCodeHelper",
    sub_agents=[scout, analyst, coder]
)
