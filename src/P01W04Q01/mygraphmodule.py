'''
Created on Nov 15, 2015

@author: Ofer
'''


class Node(object):
    def __init__(self, node_id=None, parent_graph=None):
        # TODO: node methods and attributes
        self._id = node_id
        self._parent = parent_graph
        self._narcs = set()  # set of arc.id values for arcs outgoing from self

    def addarc(self, arc):
        self._narcs.add(arc.id)

    @property
    def id(self):
        return self._id

    def getid(self):
        return self._id

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent_graph):
        self._parent = parent_graph

    @staticmethod
    def strint_to_node(str_input):
        int_input = int(str_input)
        node_object = Node(node_id=int_input)
        return node_object


class Arc(object):
    # TODO: not sure how to implement this one yet.
    """ accepts two nodes and creates an Arc instance """

    def __init__(self, node_s, node_t):
        if (not isinstance(node_s, Node) or
                not isinstance(node_t, Node)):
            raise TypeError

        # else: both nodes are of the Node class
        self._arc = tuple([node_s, node_t])

    @property
    def id(self):
        return "({}, {})".format(self.s.id, self.t.id)

    @property
    def s(self):
        return self._arc[0]

    @property
    def t(self):
        return self._arc[1]


class MyDiGraph(object):
    '''
    >>> G = mgm.DiGraph()
    >>> G.add_arc(1,2)    # set of tuples,
                          # nodes[node 1]: set(arc(1,2), more arcs)
    >>> G.add_node(42)    # dictionary key.
    >>> print(sorted(G.nodes()))
    [1, 2, 42]
    >>> print(sorted(G.edges()))
    [(1, 2)]
    '''

    def __init__(self):
        self._nodes = {}
        self._arcs = {}

    def dfs_loop(self):
        """DFS for SCC"""
        
        t = 0  # 1st pass finishing times / # of nodes processed so far
        s = None  # leaders in 2nd pass / current source vertex
        
        for i, node in enumerate(self.nodes.keys()): 
            # i = n down to 1:
            if not node.explored:
                s = len(self.nodes.keys())-i
                DFS(self, i)
                
DFS(graph G, node i):
    mark i as explored   // for rest of calling DFS-Loop function
    set leader(i) = node s
    for every arc (i, j) in G:
        if j not yet explored:
            DFS(G, j)
    t++
    set f(i) = t   // i's finishing time

    
    
    
    
    def add_arc(self, arc):
        # TODO: reorganize data-structure
        """
        nodes[arc.s]: set(arc(1,2), more arcs)
        """
        if not isinstance(arc, Arc):
            raise TypeError

        # else: input is a two node arc
        if arc.id not in self._arcs:
            self._arcs[arc.id] = arc
            # TODO: valid input check-ups
            for node in (arc.s, arc.t):
                if node.id not in self._nodes:
                    self._nodes[node.id] = node
                    node.parent = self  # TODO: is this going to work?

            arc.s.addarc(arc)  # figure this one out

    def add_node(self, node):
        # TODO: add_node()
        raise NotImplementedError("add_node")

    @property
    def nodes(self):
        return self._nodes.keys()

    @property
    def arcs(self):
        return self._arcs






    @property
    def reversed_graph(self):
        return self._reversed
