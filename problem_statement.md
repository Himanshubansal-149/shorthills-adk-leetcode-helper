# Problem Statement: LeetCode Contest Helper (Multi-Agent System)

## 🎯 Project Objective
The goal of this project is to leverage the Google Agent Development Kit (ADK) to build an autonomous system that assists competitive programmers. The system automates the process of fetching contest data, identifying algorithmic patterns, and generating implementation boilerplates.

## 🏗️ Multi-Agent Architecture
This system utilizes a **Sequential Orchestration** pattern to ensure a dependable data pipeline:

1.  **Scout Agent**: Acts as the research arm, using the `Google Search` tool to retrieve the latest LeetCode contest details.
2.  **Analyst Agent**: Serves as the logic engine, identifying DSA patterns (e.g., Dynamic Programming, Graphs) and calculating time complexity using a custom tool.
3.  **Coder Agent**: Acts as the implementation specialist, generating C++ code templates and compiling a final markdown report for the user.

## 🛠️ Technical Requirements Met
- **Root Orchestrator**: Manages the lifecycle and state of 3 sub-agents.
- **Mandatory Tools**: Integrated built-in `Google Search`.
- **Custom Tools**: Created 3 Python-based tools for logic and reporting.
- **Stable Models**: Utilizes `gemini-1.5-flash` for high-speed, reliable inference.
