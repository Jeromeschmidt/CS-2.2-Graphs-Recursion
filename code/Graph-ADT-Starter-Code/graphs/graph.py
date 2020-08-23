from collections import deque
import random

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.

        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.id = vertex_id
        self.neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.neighbors_dict[vertex_obj.id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.neighbors_dict.keys())
        return f'{self.id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.vertex_dict = {} # id -> object
        self.is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.

        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        self.vertex_dict[vertex_id] = Vertex(vertex_id)
        return self.vertex_dict[vertex_id]


    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.vertex_dict:
            return None

        vertex_obj = self.vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        if self.is_directed == True:
            self.vertex_dict[vertex_id1].add_neighbor(self.vertex_dict[vertex_id2])
        else:
            self.vertex_dict[vertex_id1].add_neighbor(self.vertex_dict[vertex_id2])
            self.vertex_dict[vertex_id2].add_neighbor(self.vertex_dict[vertex_id1])

    def get_vertices(self):
        """
        Return all vertices in the graph.

        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.vertex_dict.values())

    def get_edges(self):
        result = list()
        for vertex_obj in self.get_vertices():
            for neighbor_obj in vertex_obj.get_neighbors():
                result.append(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')
        return result

    def contains_id(self, vertex_id):
        return vertex_id in self.vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def is_bipartite(self):
        """
        Return True if the graph is bipartite, and False otherwise.
        """
        start_vertex = self.get_vertex(random.choice(list(self.vertex_dict.keys())))

        visited_vertices = set()
        next_vertices = deque()
        colors = dict()

        visited_vertices.add(start_vertex)
        next_vertices.append(start_vertex)
        colors[start_vertex] = 1

        while len(next_vertices) > 0:
            temp = next_vertices.popleft()
            visited_vertices.add(temp)
            for vert in temp.get_neighbors():
                if vert in colors and colors[vert] == colors[temp]:
                    return False
                else:
                    colors[vert] = colors[temp] * -1
                if vert not in visited_vertices:
                    next_vertices.append(vert)

        return True

    def get_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """
        connected_components = list()
        vertices_id = list(set(self.vertex_dict.keys()))
        visited_vertices = set()

        for vert_id in vertices_id:
            if vert_id not in visited_vertices:
                result = list(self.bfs_traversal(vert_id))
                connected_components.append(result)
                for elm in result:
                    visited_vertices.add(elm)

        return connected_components

    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """
        if self.contains_id(start_id) is False or self.contains_id(target_id) is False:
            raise KeyError("One or both vertices are not in the graph!")

        visited_vertices = dict()
        next_vertices = deque()

        visited_vertices[self.get_vertex(start_id)] = list()
        next_vertices.append(self.get_vertex(start_id))
        target_distance_vertices = list()

        while len(next_vertices) > 0:
            temp = next_vertices.pop()

            for neighbor in temp.get_neighbors():
                if neighbor not in visited_vertices:
                    current_path = visited_vertices[temp]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor]
                    if neighbor.get_id() == target_id:
                        target_distance_vertices.append(neighbor.get_id())
                    visited_vertices[neighbor] = next_path
                    next_vertices.append(neighbor)
        result = list()
        for elm in visited_vertices.keys():
            result.append(elm.get_id())
        return result

    def dfs_traversal(self, start_id):
        """Visit each vertex, starting with start_id, in DFS order."""

        pass

    def contains_cycle(self):
        """
        Return True if the directed graph contains a cycle, False otherwise.
        """
        if self.is_directed is False and len(self.get_edges() > 0):
            return False

        for vert in self.get_vertices():

        pass

    def topological_sort(self):
        """
        Return a valid ordering of vertices in a directed acyclic graph.
        If the graph contains a cycle, throw a ValueError.
        """
        # TODO: Create a stack to hold the vertex ordering.
        # TODO: For each unvisited vertex, execute a DFS from that vertex.
        # TODO: On the way back up the recursion tree (that is, after visiting a
        # vertex's neighbors), add the vertex to the stack.
        # TODO: Reverse the contents of the stack and return it as a valid ordering.
        pass

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if self.contains_id(start_id) is False:
            raise KeyError("One or both vertices are not in the graph!")

        visited_vertices = set()
        next_vertices = deque()

        # visited_vertices.add(self.get_vertex(start_id))
        # next_vertices.append(self.get_vertex(start_id))
        visited_vertices.add(start_id)
        next_vertices.append(start_id)

        while len(next_vertices) > 0:
            temp = next_vertices.popleft()
            visited_vertices.add(temp)
            for vert in self.get_vertex(temp).get_neighbors():
                if vert.get_id() not in visited_vertices:
                    next_vertices.append(vert.get_id())

        return visited_vertices

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if self.contains_id(start_id) is False:
            raise KeyError("One or both vertices are not in the graph!")

        visited_vertices = dict()
        next_vertices = deque()

        visited_vertices[self.get_vertex(start_id)] = list()
        next_vertices.append(self.get_vertex(start_id))

        while len(next_vertices) > 0:
            temp = next_vertices.popleft()

            if self.get_vertex(target_id) in temp.get_neighbors():
                return visited_vertices[self.get_vertex(start_id)]#[1:]

            visited_vertices[self.get_vertex(start_id)].append(temp)

            for vert in temp.get_neighbors():
                if vert not in visited_vertices[self.get_vertex(start_id)]:
                    next_vertices.append(vert)

        return None

    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.

        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for

        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """
        visited_vertices = dict()
        next_vertices = deque()

        visited_vertices[self.get_vertex(start_id)] = list()
        next_vertices.append(self.get_vertex(start_id))
        target_distance_vertices = list()

        while len(next_vertices) > 0:
            temp = next_vertices.popleft()

            for neighbor in temp.get_neighbors():
                if neighbor not in visited_vertices:
                    current_path = visited_vertices[temp]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor]
                    if len(next_path) == target_distance:
                        target_distance_vertices.append(neighbor.get_id())
                    visited_vertices[neighbor] = next_path
                    next_vertices.append(neighbor)

        return target_distance_vertices
