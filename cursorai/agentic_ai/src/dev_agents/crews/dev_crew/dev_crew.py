from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class DevCrew():
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def junior_dev(self) -> Agent:
		return Agent(
			config=self.agents_config['junior_dev'],
		)

	@agent	
	def senior_dev(self) -> Agent:
		return Agent(
			config=self.agents_config['senior_dev'],
		)

	@task
	def write_code(self) -> Task:
		return Task(
			config=self.tasks_config['write_code'],
		)

	@task
	def review_code(self) -> Task:
		return Task(
			config=self.tasks_config['review_code'],
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
