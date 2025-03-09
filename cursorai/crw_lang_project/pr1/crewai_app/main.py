from crewai import Crew
from common.config import OPENAI_API_KEY
from .agents import AgentFactory
from .tasks import TaskFactory

def run_crew_workflow():
    # Initialize agent factory
    agent_factory = AgentFactory()

    # Create agents
    researcher = agent_factory.create_researcher()
    writer = agent_factory.create_writer()

    # Create tasks
    research_task = TaskFactory.create_research_task(
        researcher, 
        "AI advancements in 2024"
    )
    
    writing_task = TaskFactory.create_writing_task(
        writer,
        "{research_task.output}"
    )

    # Create and run the crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=2
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
    result = run_crew_workflow()
    print("\nFinal Result:")
    print(result) 