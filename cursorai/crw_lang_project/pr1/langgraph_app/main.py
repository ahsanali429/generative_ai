from common.config import OPENAI_API_KEY
from .graph import create_workflow

def run_langgraph_workflow():
    # Create the workflow
    workflow = create_workflow()

    # Initialize state
    initial_state = {
        "messages": [],
        "current_step": 0
    }

    # Run the workflow
    result = workflow.invoke(initial_state)
    return result

if __name__ == "__main__":
    result = run_langgraph_workflow()
    print("\nFinal Result:")
    print(result) 