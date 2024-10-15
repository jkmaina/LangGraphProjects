# LangGraphProjects - Lesson 1A: Hello World with LangGraph

This project provides a basic introduction to using LangGraph to build a simple AI agent. It demonstrates the fundamentals of defining nodes, states, and edges, and visualizing the execution flow with Mermaid. The goal of this lesson is to create a basic "Hello World" state graph in LangGraph.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup and Requirements](#setup-and-requirements)
3. [Code Explanation](#code-explanation)
4. [Running the Code](#running-the-code)
5. [Visualizing the Graph](#visualizing-the-graph)

---

## Project Overview

This lesson covers:
- Defining a state using `TypedDict` to store data.
- Creating a LangGraph state graph with a node and defining edges between nodes.
- Compiling and executing the graph.
- Visualizing the graph using Mermaid to better understand its flow.

## Setup and Requirements

Before running this project, ensure you have the following installed:
- Python 3.7+
- Required packages: `langgraph`, `typing_extensions`

Install the required packages with the following command:
```bash
pip install langgraph typing_extensions
```
## Code Explanation

### 1. Defining the State

We use `TypedDict` to define the state of the graph. This state will store a `greeting` message.

```python
from typing_extensions import TypedDict

class HelloWorldState(TypedDict):
    greeting: str
```

### 2. Creating a Node Function

The function `hello_world_node` is the core node in this graph. It takes the state as input, appends a "Hello World" message to it, and returns the updated state.

```python
def hello_world_node(state: HelloWorldState):
    state["greeting"] = "Hello World, " + state["greeting"]
    return state

```

### 3. Building the Graph

We initialize the graph using `StateGraph`, add the `hello_world_node`, and define the flow with `add_edge`. This configuration sets up the flow of execution for the graph, where the process starts, moves to the "greet" node, and then finishes.

```python
from langgraph.graph import StateGraph, START, END

builder = StateGraph(HelloWorldState)
builder.add_node("greet", hello_world_node)
builder.add_edge(START, "greet")  # Connect START to the "greet" node
builder.add_edge("greet", END)    # Connect the "greet" node to END
```

### 4. Compiling and Executing the Graph

After defining the graph, the next step is to compile it, which prepares it for execution. Once compiled, we invoke the graph with an initial state. In this example, the initial state includes a greeting message. The result of invoking the graph is printed, displaying the final output.

```python
graph = builder.compile()
result = graph.invoke({"greeting": "from LangGraph!"})
print(result)  # Output: {'greeting': 'Hello World, from LangGraph!'}
```

In this case, the output should be:


```python
{'greeting': 'Hello World, from LangGraph!'}
```

This confirms that the "greet" node has processed the input and appended "Hello World" to the greeting.

### 5. Visualizing the Graph

To better understand the structure and flow of the graph, you can visualize it using Mermaid. This will generate a PNG image that displays the nodes and edges, representing the flow from start to end within the graph.

![Workflow Graph](./graph_20916.png)


```python
from langchain_core.runnables.graph import MermaidDrawMethod
import os
import random

# Generate a visual representation of the graph in PNG format
mermaid_png = graph.get_graph(xray=1).draw_mermaid_png(draw_method=MermaidDrawMethod.API)

# Specify the output folder and save the image with a unique filename
output_folder = "."
os.makedirs(output_folder, exist_ok=True)
filename = os.path.join(output_folder, f"graph_{random.randint(1, 100000)}.png")

with open(filename, 'wb') as f:
    f.write(mermaid_png)

```
The PNG file will be saved in the current directory under a randomly generated name, such as graph_12345.png. You can manually open this file to see the graph's structure.

Alternatively, you can use the following code snippet to automatically open the generated image, depending on your operating system:

```python
import subprocess
import sys

if sys.platform.startswith('darwin'):   # For macOS
    subprocess.call(('open', filename))
elif sys.platform.startswith('linux'):  # For Linux
    subprocess.call(('xdg-open', filename))
elif sys.platform.startswith('win'):    # For Windows
    os.startfile(filename)
```

By visualizing the graph, you can confirm how nodes are interconnected and gain insight into the agent's flow from start to finish. This step is valuable for debugging and understanding the behavior of more complex AI agents as you continue to develop with LangGraph.

To proceed further, explore adding more nodes and edges or modifying the graph to perform different tasks. Visualization tools like Mermaid help you keep track of these changes and ensure your graph operates as intended.

Happy Coding!