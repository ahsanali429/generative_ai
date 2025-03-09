from crewai.flow.flow import Flow, start, listen

class SimpleFlow(Flow):

    @start()
    def func1(self):
        print("Step1: Func1")
        return "Step1: Func1";

    @listen(func1)
    def func2(self):
        print("Step2: Func2")
        return "Step1: Func1";

    @listen(func2)
    def func3(self):
        print("Step3: Func3")
        return {"message": "Flow Completed!!!"}

def run():
    obj = SimpleFlow()
    result = obj.kickoff() 
    return result