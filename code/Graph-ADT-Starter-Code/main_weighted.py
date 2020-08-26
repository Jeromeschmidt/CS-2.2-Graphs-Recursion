from graphs.weighted_graph import WeightedGraph
from util.file_reader import read_graph_from_file
# from graphs.weighted_graph import WeightedGraph


# Driver code
if __name__ == '__main__':

    # Create the graph

    graph = WeightedGraph(is_directed=False)
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_c = graph.add_vertex('D')
    vertex_c = graph.add_vertex('E')
    vertex_c = graph.add_vertex('F')
    vertex_c = graph.add_vertex('G')
    vertex_c = graph.add_vertex('H')
    vertex_c = graph.add_vertex('J')

    graph.add_edge('A','B', 4)
    graph.add_edge('A','C', 8)
    graph.add_edge('B','C', 11)
    graph.add_edge('B','D', 8)
    graph.add_edge('C','F', 1)
    graph.add_edge('C','E', 4)
    graph.add_edge('D','E', 2)
    graph.add_edge('D','G', 7)
    graph.add_edge('D','H', 4)
    graph.add_edge('E','F', 6)
    graph.add_edge('F','H', 2)
    graph.add_edge('G','H', 14)
    graph.add_edge('G','J', 9)
    graph.add_edge('H','J', 10)

    # Or, read a graph in from a file
    # graph = read_graph_from_file('test_files/graph_small_directed.txt')
    print(graph)

    # Output the vertices & edges
    # Print vertices
    print(f'The vertices are: {graph.get_vertices()} \n')

    # Print edges
    print('The edges are:')
    # for vertex_obj in graph.get_vertices():
    #     for neighbor_obj in vertex_obj.get_neighbors():
    #         print(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')
    print(sorted(graph.get_edges(), key=lambda x: x[2]))

    # Search the graph
    print('Performing BFS traversal...')
    graph.bfs_traversal('A')

    # Find shortest path
    print('Finding shortest path from vertex A to vertex E...')
    shortest_path = graph.find_shortest_path('A', 'E')
    print(shortest_path)

    # Find all vertices N distance away
    print('Finding all vertices distance 2 away...')
    vertices_2_away = graph.find_vertices_n_away('A', 2)
    print(vertices_2_away)

    print(graph.get_connected_components())

    # print(graph.dfs_traversal('A'))

    print("!!!")
    print(graph.contains_cycle())
