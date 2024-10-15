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
