from typing import Dict, TypedDict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

class AgentState(TypedDict):
    messages: list
    current_step: int

def create_research_node():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    def research(state: AgentState) -> AgentState:
        messages = state["messages"]
        response = llm.invoke(
            messages + [HumanMessage(content="Research the latest AI advancements")]
        )
        return {
            "messages": messages + [HumanMessage(content="Research the latest AI advancements"), response],
            "current_step": state["current_step"] + 1
        }
    
    return research

def create_analysis_node():
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    def analyze(state: AgentState) -> AgentState:
        messages = state["messages"]
        last_research = messages[-1].content
        response = llm.invoke(
            messages + [HumanMessage(content=f"Analyze these findings: {last_research}")]
        )
        return {
            "messages": messages + [HumanMessage(content=f"Analyze findings"), response],
            "current_step": state["current_step"] + 1
        }
    
    return analyze 