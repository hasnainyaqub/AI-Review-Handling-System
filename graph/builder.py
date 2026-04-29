from langgraph.graph import StateGraph, START, END

from graph.edges.conditional import sentiment_router
from graph.nodes.diagnoses import run_diagnoses
from graph.nodes.negative import negative_response
from graph.nodes.positive import positive_response
from graph.nodes.sentiment import sentiment_find
from graph.state import ReviewInputState

def build_graph():

    graph = StateGraph(ReviewInputState)

    graph.add_node('sentiment_find', sentiment_find)
    graph.add_node('positive_response', positive_response)
    graph.add_node('run_diagnoses', run_diagnoses)
    graph.add_node('negative_response', negative_response)

    graph.add_edge(START, 'sentiment_find')
    graph.add_conditional_edges('sentiment_find', sentiment_router)      
    graph.add_edge('positive_response', END)

    graph.add_edge('run_diagnoses', 'negative_response')
    graph.add_edge('negative_response', END)

    return graph.compile()
