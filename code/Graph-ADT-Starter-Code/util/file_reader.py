# from graphs.graph import Graph
# import sys
# sys.path.append('/Users/jeromeschmidt/dev/ms/CS-2.2-Graphs-Recursion/code/Graph-ADT-Starter-Code/')
from pathlib import Path

from graphs.graph import Graph

def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """

    # TODO: Use 'open' to open the file
    filename = "../"+filename
    path = Path(__file__).parent / filename
    with path.open() as f:
        lines = f.readlines()
    f.close()
    # TODO: Use the first line (G or D) to determine whether graph is directed
    # and create a graph object
    if lines[0][:len(lines[0])-1] is "D":
        graph = Graph(is_directed=True)
    elif lines[0][:len(lines[0])-1] is "G":
        graph = Graph(is_directed=False)
    else:
        raise ValueError("Invalid Graph Type")
    # TODO: Use the second line to add the vertices to the graph
    vertices = lines[1][:len(lines[1])-1].split(",")
    for elm in vertices:
        graph.add_vertex(elm)
    # TODO: Use the 3rd+ line to add the edges to the graph
    for i in range(2,len(lines)):
        elm = lines[i][:len(lines[i])]
        graph.add_edge(elm[1], elm[3])

    return graph
