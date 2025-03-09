from langgraph.func import task, entrypoint
import litellm

@task
def func1():
	response = litellm.completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Give me any city name, only"}]
    )
    return response["choices"][0]["message"]["content"]

@task
def func2():
	return "Step2: Func2"

@task
def func3():
	return "Step3: Func3"

@entrypoint()
def simple_flow(input) -> dict:
	o1 = func1().result()
	o2 = func2().result()
	o3 = func3().result()
	return {"o1": o1, "o2": o2, "o3": o3};

def run_simple_flow():
	result = simple_flow.invoke(input="Pakistan")
	print(result)