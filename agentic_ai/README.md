# Dev Agentic Crew

Welcome to **Dev Agentic**, a multi-agent AI system powered by [crewAI](https://crewai.com). This project features two AI agents collaborating on Python development:

- **Junior Dev Agent** → Generates Python code  
- **Senior Dev Agent** → Reviews, refactors, and applies best practices  

## Installation

Ensure you have **Python >=3.10 <=3.13** installed. Install dependencies using:

```bash
pip install uv
crewai install
```

## Customization

- Define agents in `src/dev_agentic/config/agents.yaml`  
- Define tasks in `src/dev_agentic/config/tasks.yaml`  
- Modify `src/dev_agentic/dev_crew.py` for logic, tools, and configurations  
- Edit `src/dev_agentic/main.py` for custom inputs  

## Running the Project

Run the AI agents with:

### From Crew:
```bash
crewai run
```
### From UV:
```bash
uv run dev-kickoff
```

This initializes the **Dev Agentic Crew**, automating code generation and review.

## Support

For help, refer to [crewAI Docs](https://docs.crewai.com) and [crewAI Flow Docs](https://docs.crewai.com/concepts/flows).
