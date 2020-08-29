from graphs.graph import Graph, Vertex

class WeightedVertex(Vertex):

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.

        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.id = vertex_id
        self.neighbors_dict = {} # id -> (obj, weight)

    def add_neighbor(self, vertex_obj, weight):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        weight (number): The weight of this edge.
        """
        if vertex_obj.get_id() in self.neighbors_dict.keys():
            return # it's already a neighbor

        self.neighbors_dict[vertex_obj.get_id()] = (vertex_obj, weight)

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return [neighbor for (neighbor, weight) in self.neighbors_dict.values()]

    def get_neighbors_with_weights(self):
        """Return the neighbors of this vertex."""
        return list(self.neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = [neighbor.get_id() for neighbor in self.get_neighbors()]
        return f'{self.id} adjacent to {neighbor_ids}'


class WeightedGraph(Graph):

    INFINITY = float('inf')

    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.vertex_dict = {}
        self.is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.

        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        if vertex_id in self.vertex_dict.keys():
            return False # it's already there
        vertex_obj = WeightedVertex(vertex_id)
        self.vertex_dict[vertex_id] = vertex_obj
        return True

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id in self.vertex_dict:
            return self.vertex_dict[vertex_id]
        return None

    def add_edge(self, vertex_id1, vertex_id2, weight):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        weight (number): The edge weight.
        """
        if vertex_id1 not in self.vertex_dict.keys() or vertex_id2 not in self.vertex_dict.keys():
            raise ValueError("One or more vertices does not exist")

        vertex_1 = self.get_vertex(vertex_id1)
        vertex_2 = self.get_vertex(vertex_id2)

        if self.is_directed is True:
            vertex_1.add_neighbor(vertex_2, weight)
        else:
            vertex_1.add_neighbor(vertex_2, weight)
            vertex_2.add_neighbor(vertex_1, weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return list(self.vertex_dict.values())

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax:
        for vertex in graph"""
        return iter(self.vertex_dict.values())

    def union(self, parent_map, vertex_id1, vertex_id2):
        """Combine vertex_id1 and vertex_id2 into the same group."""
        vertex1_root = self.find(parent_map, vertex_id1)
        vertex2_root = self.find(parent_map, vertex_id2)
        parent_map[vertex1_root] = vertex2_root


    def find(self, parent_map, vertex_id):
        """Get the root (or, group label) for vertex_id."""
        if(parent_map[vertex_id] == vertex_id):
            return vertex_id
        return self.find(parent_map, parent_map[vertex_id])

    def get_edges(self):
        result = list()
        for vertex_obj in self.get_vertices():
            for neighbor_obj, weight in vertex_obj.get_neighbors_with_weights():
                result.append((vertex_obj.get_id() , neighbor_obj.get_id(), weight))
        return result

    def minimum_spanning_tree_kruskal(self):
        """
        Use Kruskal's Algorithm to return a list of edges, as tuples of
        (start_id, dest_id, weight) in the graph's minimum spanning tree.
        """
        # TODO: Create a list of all edges in the graph, sort them by weight
        # from smallest to largest
        all_edges = sorted(self.get_edges(), key=lambda x: x[2])
        # TODO: Create a dictionary `parent_map` to map vertex -> its "parent".
        # Initialize it so that each vertex is its own parent.
        parent_map = dict()
        for vert in self.get_vertices():
            parent_map[vert.get_id()] = vert.get_id()
        # TODO: Create an empty list to hold the solution (i.e. all edges in the
        # final spanning tree)
        result = list()
        # TODO: While the spanning tree holds < V-1 edges, get the smallest
        # edge. If the two vertices connected by the edge are in different sets
        # (i.e. calling `find()` gets two different roots), then it will not
        # create a cycle, so add it to the solution set and call `union()` on
        # the two vertices.
        for edge in all_edges:
            if self.find(parent_map, edge[0]) != self.find(parent_map, edge[1]):
                result.append(edge)
                self.union(parent_map, edge[0], edge[1])
        # TODO: Return the solution list.
        return result

    def get_minimum_weight(self, vertex_to_weight):
        min = (None, float('inf'))

        for key, value in vertex_to_weight.items():
            if value < min[1]:
                min = (key, value)
        return min

    def minimum_spanning_tree_prim(self):
        """
        Use Prim's Algorithm to return the total weight of all edges in the
        graph's spanning tree.

        Assume that the graph is connected.
        """
        # TODO: Create a dictionary `vertex_to_weight` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`
        MST = 0
        visited = set()
        vertex_to_weight = dict()
        vertices = self.get_vertices()
        for vert in self.get_vertices():
            vertex_to_weight[vert.get_id()] = float('inf')
        # TODO: Choose one vertex and set its weight to 0
        vertex_to_weight[vertices[0].get_id()] = 0
        # TODO: While `vertex_to_weight` is not empty:
        # 1. Get the minimum-weighted remaining vertex, remove it from the
        #    dictionary, & add its weight to the total MST weight
        # 2. Update that vertex's neighbors, if edge weights are smaller than
        #    previous weights
        while vertex_to_weight != {}:
            min = self.get_minimum_weight(vertex_to_weight)
            vertex_to_weight.pop(min[0])
            MST += min[1]
            visited.add(min[0])

            for neighbor, weight in self.get_vertex(min[0]).get_neighbors_with_weights():
                if neighbor.get_id() not in visited:
                    if weight < vertex_to_weight[neighbor.get_id()]:
                        vertex_to_weight[neighbor.get_id()] = weight

        # TODO: Return total weight of MST
        return MST

    def find_shortest_path(self, start_id, target_id):
        """
        Use Dijkstra's Algorithm to return the total weight of the shortest path
        from a start vertex to a destination.
        """
        # TODO: Create a dictionary `vertex_to_distance` and initialize all
        # vertices to INFINITY - hint: use `float('inf')`
        visited = set()
        vertex_to_distance = dict()
        for vert in self.get_vertices():
            vertex_to_distance[vert.get_id()] = float('inf')
        # TODO: While `vertex_to_distance` is not empty:
        # 1. Get the minimum-distance remaining vertex, remove it from the
        #    dictionary. If it is the target vertex, return its distance.
        # 2. Update that vertex's neighbors by adding the edge weight to the
        #    vertex's distance, if it is lower than previous.
        vertex_to_distance[start_id] = 0

        while vertex_to_distance != {}:
            min = self.get_minimum_weight(vertex_to_distance)

            visited.add(min[0])
            if min[0] == target_id:
                return vertex_to_distance[target_id]
            vertex_to_distance.pop(min[0])
            for neighbor, weight in self.get_vertex(min[0]).get_neighbors_with_weights():
                if neighbor.get_id() not in visited:
                    if weight < vertex_to_distance[neighbor.get_id()]:
                        vertex_to_distance[neighbor.get_id()] = weight + min[1]


        # TODO: Return None if target vertex not found.
        return None

    def floyd_warshall(self):
        """
        Return the All-Pairs-Shortest-Paths dictionary, containing the shortest
        paths from each vertex to each other vertex.
        """
        shortest_paths = dict()
        for vert_1 in self.get_vertices():
            for vert_2 in self.get_vertices():
                if vert_1 != vert_2:
                    shortest_paths[vert_1] = self.find_shortest_path(vert_2)

        return shortest_paths
