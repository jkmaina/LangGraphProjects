import os
import subprocess
import sys
from langchain_core.runnables.graph import MermaidDrawMethod
import random 

def display_graph(graph, output_folder="output"):

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

