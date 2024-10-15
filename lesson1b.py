#lesson1b.py
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables.graph import MermaidDrawMethod
from  display_graph import display_graph


# Define the state structure
class HelloWorldState(TypedDict):
    greeting: str  # This key will store the greeting message

# Define an additional node function
def exclamation_node(state: HelloWorldState):
    state["greeting"] += "!"
    return state

# Define the node function
def hello_world_node(state: HelloWorldState):
    state["greeting"] = "Hello World, " + state["greeting"]
    return state

# Initialize the graph and add the node
builder = StateGraph(HelloWorldState)
builder.add_node("greet", hello_world_node)

# Define the flow of execution using edges
builder.add_edge(START, "greet")  # Connect START to the "greet" node
builder.add_node("exclaim", exclamation_node) # Add a new node

# Update the edges
builder.add_edge("greet", "exclaim")  # Connect "greet" to "exclaim"
builder.add_edge("exclaim", END)      # Update the flow to end after "exclaim"


# Compile and run the graph
graph = builder.compile()
result = graph.invoke({"greeting": "from LangGraph!"})

# Output the result
print(result)
# Output: {'greeting': 'Hello World, from LangGraph!!'}

#Visualise the graph
display_graph(graph)