'''
Created on Nov 15, 2015

@author: Ofer
'''


class Node(object):
    def __init__(self, node_id=None, parent_graph=None):
        # TODO: node methods and attributes
        self._id = node_id
        self._parent = parent_graph

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
        # TODO: is it possible to use a mutable inside a tuple?
        self._s = node_s
        self._t = node_t
        self._arc = tuple([node_s, node_t])

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
        self._arcs = set()

    def add_arc(self, arc):
        # TODO: reorganize data-structure
        """
        nodes[arc.s]: set(arc(1,2), more arcs)
        """
        if not isinstance(arc, Arc):
            raise TypeError

        # else: input is a two node arc
        if arc not in self._arcs:
            self._arcs.add(arc)
            # TODO: dict/set input check-ups
            for node in (arc.s, arc.t):
                if node not in self._nodes:
                    self._nodes[node] = set()

            self._nodes[arc.s].add(arc)

    def add_node(self, node):
        # TODO: add_node()
        raise NotImplementedError("add_node")

    @property
    def nodes(self):
        return self._nodes.keys()

    @property
    def arcs(self):
        return self._arcs
