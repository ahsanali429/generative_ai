from langgraph.graph import Graph
from typing import Dict, TypedDict
from .nodes import create_research_node, create_analysis_node

def create_workflow() -> Graph:
    # Create nodes
    research = create_research_node()
    analyze = create_analysis_node()

    # Create workflow
    workflow = Graph()

    # Add nodes
    workflow.add_node("research", research)
    workflow.add_node("analyze", analyze)

    # Add edges
    workflow.add_edge("research", "analyze")

    # Set entry point
    workflow.set_entry_point("research")

    return workflow.compile() 