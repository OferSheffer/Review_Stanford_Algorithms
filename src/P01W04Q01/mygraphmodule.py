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

    def __init__(self, node_s, node_t):
        if (not isclass(node_s, Node) or
                not isclass(node_t, Node)):
            raise ValueError

        # else: both nodes are of the Node class
        self._arc = tuple(node_s, node_t)


class MyDiGraph(object):
    '''
    >>> G=mgm.Graph()
    >>> G.add_edge(1,2)
    >>> G.add_node(42)
    >>> print(sorted(G.nodes()))
    [1, 2, 42]
    >>> print(sorted(G.edges()))
    [(1, 2)]
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._nodes = {}
        self._arcs = set()

    def add_arc(self, arc):
        """assumes legitimate input"""
        if not isclass(arc, Arc):
            raise ValueError
        # else: input is a two node arc
        if arc not in self._arcs:
            self._arcs.add(arc)
            # TODO: add dict related checkups
            
        