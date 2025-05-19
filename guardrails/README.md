# 🛡️ Guardrails for Generative AI

This repo demonstrates using guardrails to restrict AI inputs to math-related tasks only, leveraging Gemini models with the `openai-agents` framework.

---

## 🚀 Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/ahsanali429/generative_ai.git
cd your-repo
````

### 2. Install dependencies

```bash
pip install -qU openai-agents "openai-agents[litellm]"
```

### 3. Set API key

Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key
```

---

## 🧑‍💻 Usage Overview

* Define a **guardrail agent** that detects if input is *not* math-related.
* Create an **input guardrail** to block non-math inputs.
* Build an **assistant agent** that only processes math queries.
* Run the assistant; if a non-math query is detected, a guardrail tripwire triggers.

---

## 📄 Core Code Explanation

```python
from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput
from agents.extensions.models.litellm_model import LitellmModel
from pydantic import BaseModel
```

* Imports essential classes and functions for building agents and guardrails.

```python
class MathHomeWorkOutput(BaseModel):
    is_not_math_related_task: bool
    reasoning: str
```

* Defines the output schema for the guardrail agent.
* It returns a flag indicating if the input is non-math related and a reasoning message.

```python
guardrail_agent = Agent(
    name="Guardrail Check",
    instructions="Check if input is not math-related.",
    model=LitellmModel(model="gemini/gemini-1.5-flash"),
    output_type=MathHomeWorkOutput
)
```

* Creates a guardrail agent that checks if the input is math-related or not using Gemini 1.5 model.

```python
@input_guardrail
async def math_guardrail(ctx, agent, input):
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_math_related_task
    )
```

* Defines an async input guardrail function that runs the guardrail agent on user input.
* If the input is not math-related (`tripwire_triggered`), it blocks the request.

```python
assistant_agent = Agent(
    name="Assistant",
    instructions="Solve math-related problems.",
    model=LitellmModel(model="gemini/gemini-2.0-flash"),
    input_guardrails=[math_guardrail]
)
```

* Defines the main assistant agent that solves math problems using Gemini 2.0 model.
* Applies the input guardrail to filter out non-math inputs.

```python
try:
    result = Runner.run_sync(assistant_agent, "Hello")
    print(result.final_output)
except InputGuardrailTripwireTriggered:
    print("Please ask only math-related questions.")
```

* Runs the assistant synchronously with sample input.
* If the guardrail trips (non-math input), it catches the exception and shows a warning message.

