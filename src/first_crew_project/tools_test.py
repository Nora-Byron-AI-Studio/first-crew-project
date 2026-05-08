"""
Day 13 CrewAI Tools Consolidation

This script demonstrates a basic multi-agent CrewAI workflow:
1. Writer agent writes content to a file.
2. Reader agent reads the file back.
3. Optional custom tool returns business hours.

Purpose:
Practice tool usage, task structure, and multi-agent execution.
"""

from crewai import Agent, Task, Crew
from crewai_tools import FileWriterTool, FileReadTool

def create_agents():
    """
    Creates the writer and reader agents with their assigned tools.

    Returns:
        tuple: writer agent and reader agent.
    """
    write_tool = FileWriterTool()
    read_tool = FileReadTool()

    writer = Agent(
        role="Writer",
        goal="Write text to a file",
        backstory="Writes outputs to files.",
        tools=[write_tool],
        verbose=True,
    )

    reader = Agent(
        role="Reader",
        goal="Read file contents",
        backstory="Reads files and returns content.",
        tools=[read_tool],
        verbose=True,
    )

    return writer, reader


def create_tasks(writer, reader):
    """
    Creates the write and read tasks for the CrewAI workflow.

    Args:
        writer: Agent responsible for writing to the file.
        reader: Agent responsible for reading from the file.

    Returns:
        list: Tasks for the crew to execute.
    """
    write_task = Task(
        description="Write 'Hello from CrewAI tools test' to output.txt using the file tool.",
        expected_output="File output.txt created with the text.",
        agent=writer,
    )

    read_task = Task(
        description="Read the contents of output.txt using the file read tool and return it.",
        expected_output="The content of the file output.txt.",
        agent=reader,
    )

    return [write_task, read_task]

def run_crew():
    """
    Builds and runs the CrewAI workflow.

    Returns:
        Any: Result returned by crew.kickoff().
    """
    writer, reader = create_agents()
    tasks = create_tasks(writer, reader)

    crew = Crew(
        agents=[writer, reader],
        tasks=tasks,
        verbose=True,
    )

    return crew.kickoff()

if __name__ == "__main__":
    result = run_crew()
    print(result)