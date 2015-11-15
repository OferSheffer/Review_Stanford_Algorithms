'''
Created on Nov 15, 2015

@author: Ofer
'''
from _pytest.python import isclass


class Node(object):
    def __init__(self, parent_graph):
        # TODO: node methods and attributes
        pass


class Arc(object):
    # TODO: not sure how to implement this one yet.

    def __init__(self, node_s, node_t):
        if (not isclass(node_s, Node) or
                not isclass(node_t, Node)):
            raise ValueError

        # else: both nodes are of the Node class
        # TODO: is it possible to use a mutable inside a tuple?
        self._s = node_s
        self._t = node_t
        self._arc = tuple(node_s, node_t)


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
        # TODO: hopefully, sets here don't take up too much memory
        """nodes[arc.s]: set(arc(1,2), more arcs)"""
        if not isclass(arc, Arc):
            raise ValueError

        # else: input is a two node arc
        if arc not in self._arcs:
            self._arcs.add(arc)
            # TODO: dict/set input check-ups
            for node in (arc.s, arc.t):
                if node not in self._nodes:
                    self._nodes[node] = set()

            self._nodes[arc.s].append(self._arcs[arc])

    def add_node(self, node):
        # TODO: add_node()
        raise NotImplementedError
