#lesson1a.py
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables.graph import MermaidDrawMethod
import os
import subprocess
import sys
import random 

# Define the state structure
class HelloWorldState(TypedDict):
    greeting: str  # This key will store the greeting message

# Define the node function
def hello_world_node(state: HelloWorldState):
    state["greeting"] = "Hello World, " + state["greeting"]
    return state

# Initialize the graph and add the node
builder = StateGraph(HelloWorldState)
builder.add_node("greet", hello_world_node)

# Define the flow of execution using edges
builder.add_edge(START, "greet")  # Connect START to the "greet" node
builder.add_edge("greet", END)    # Connect the "greet" node to END

# Compile and run the graph
graph = builder.compile()
result = graph.invoke({"greeting": "from LangGraph!"})

# Output the result
print(result)
# Output: {'greeting': 'Hello World, from LangGraph!'}

#Code to visualise the graph, we will use this in all lessons
mermaid_png = graph.get_graph(xray=1).draw_mermaid_png(draw_method=MermaidDrawMethod.API)
    
# Create output folder if it doesn't exist
output_folder = "."
os.makedirs(output_folder, exist_ok=True)

filename = os.path.join(output_folder, f"graph_{random.randint(1, 100000)}.png")
with open(filename, 'wb') as f:
    f.write(mermaid_png)

if sys.platform.startswith('darwin'):
    subprocess.call(('open', filename))
elif sys.platform.startswith('linux'):
    subprocess.call(('xdg-open', filename))
elif sys.platform.startswith('win'):
    os.startfile(filename)