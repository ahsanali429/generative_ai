from crewai import Task

class TaskFactory:
    @staticmethod
    def create_research_task(agent, topic):
        return Task(
            description=f"Research the following topic thoroughly: {topic}",
            agent=agent,
            context="Gather comprehensive information and key insights",
            expected_output="Detailed research findings in a structured format"
        )

    @staticmethod
    def create_writing_task(agent, research_output):
        return Task(
            description="Create a well-structured article based on the research",
            agent=agent,
            context=f"Use this research to create content: {research_output}",
            expected_output="A complete article with introduction, main points, and conclusion"
        ) 