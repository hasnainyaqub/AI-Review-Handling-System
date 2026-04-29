from graph.builder import build_graph

graph = build_graph()

def run_agent(input_data: dict):
    result = graph.invoke(input_data)

    # extract only useful part
    if "response" in result:
        return {"response": result["response"].content}

    return result