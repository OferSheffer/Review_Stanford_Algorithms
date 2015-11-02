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

    def __init__(self, graph={}, edges=[]):
        """ initializes a graph object """
        self._graph = copy.deepcopy(graph)
        self._edges = copy.deepcopy(edges)
        # TODO: test this
        if self._graph and len(edges) is 0:
            self.generate_edges()

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self._graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self._edges

    def generate_edges(self):
        # TODO: test this
        assert len(self._edges) is 0
        # TODO: test this
        for node in self._graph:
            for neighbour in self._graph[node]:
                self._edges.append((node, neighbour))

    def find_isolated_nodes(self):
        # TODO: test this
        """ returns a list of isolated nodes. """
        self._isolated = []
        for node in self._graph:
            if not self._graph[node]:
                self._isolated += node
        return self._isolated