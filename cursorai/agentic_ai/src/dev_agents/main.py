#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from .crews.dev_crew.dev_crew import DevCrew


class DevState(BaseModel):
    problem_statement: str = ''
    code: str = ''


class DevFlow(Flow[DevState]):

    @start()
    def start_dev(self):
        print("Starting dev")
        self.state.problem_statement = 'addition of 2 numbers'

    @listen(start_dev)
    def generate_review_code(self):
        print("Generating & Revewing Code")
        result = (
            DevCrew()
            .crew()
            .kickoff(inputs={"problem_statement": self.state.problem_statement})
        )
        print("Code generated", result.raw)
        self.state.code = result.raw

def kickoff():
    dev_flow = DevFlow()
    dev_flow.kickoff()


def plot():
    dev_flow = DevFlow()
    dev_flow.plot()

if __name__ == "__main__":
    kickoff()