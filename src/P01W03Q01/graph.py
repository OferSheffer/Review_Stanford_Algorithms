import copy

class Graph(object):
    """
    graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
    """

    def __init__(self, graph={}):
        """ initializes a graph object """
        self._graph = copy.deepcopy(graph)
        self._generate_edges()

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self._graph.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self._edges
    
    def _generate_edges(self):
        """ initialization - generate edges """
        # TODO: test this
        self._edges = []
        for node in self._graph:
            for neighbour in self._graph[node]:
                self._edges.append((node, neighbour))
    
    def add_vertex(self, vertex):
        # TODO: test this
        if vertex not in self._graph:
            self._graph[vertex] = []

    def add_edge(self, edge):
        # TODO: test this
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self._graph:
            self._graph[vertex1].append(vertex2)
        else:
            self._graph[vertex1] = [vertex2]
    
    def __str__(self):
        res = "vertices: "
        for k in self._graph:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        return res

    def find_isolated_nodes(self):
        # TODO: test this
        """ returns a list of isolated nodes. """
        self._isolated = []
        for node in self._graph:
            if not self._graph[node]:
                self._isolated += node
        return self._isolated


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = Graph(g)

    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print("Add vertex:")
    graph.add_vertex("z")

    print("Vertices of graph:")
    print(graph.vertices())
 
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())

    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())