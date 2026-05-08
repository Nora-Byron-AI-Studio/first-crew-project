🧠 CrewAI Tools Workflow (Day 12–13)
📌 Overview

This project demonstrates a basic multi-agent workflow using CrewAI.

It shows how agents can:

Write data to a file
Read data from a file
Use custom tools
⚙️ What It Does

The workflow includes 3 agents:

Writer Agent
Uses FileWriterTool
Writes text to output.txt
Reader Agent
Uses FileReadTool
Reads the content of output.txt
Assistant Agent (Custom Tool)
Uses a custom tool
Returns business hours
🏗️ Project Structure
src/
  first_crew_project/
    tools_test.py
    output.txt
🚀 How to Run
1. Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate
2. Install dependencies
pip install crewai crewai-tools python-dotenv
3. Run the script
python tools_test.py
📄 Example Output
Hello from CrewAI tools test
⚠️ Issues Faced
Missing pip in virtual environment
regex build error during install
Missing expected_output in CrewAI Task
Missing tool imports (FileReadTool)
📚 Key Learnings
CrewAI requires explicit task structure (expected_output)
Agents must be clearly instructed to use tools
Tools enable real actions (not just LLM responses)
Multi-agent workflows pass data between tasks