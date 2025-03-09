from crewai import Agent
from langchain_openai import ChatOpenAI

class AgentFactory:
    def __init__(self, model="gpt-3.5-turbo"):
        self.llm = ChatOpenAI(
            model=model,
            temperature=0.7
        )

    def create_researcher(self):
        return Agent(
            role='Research Analyst',
            goal='Conduct thorough research and analysis',
            backstory='Expert at gathering and analyzing information',
            llm=self.llm,
            verbose=True
        )

    def create_writer(self):
        return Agent(
            role='Content Writer',
            goal='Create well-written and engaging content',
            backstory='Experienced writer with expertise in creating clear and compelling content',
            llm=self.llm,
            verbose=True
        ) 