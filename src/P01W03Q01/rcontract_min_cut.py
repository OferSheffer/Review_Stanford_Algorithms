'''
Created on Nov 1, 2015

@author: Ofer

Question 1
Download the text file here. (Right click and save link as)
http://spark-public.s3.amazonaws.com/algo1/programming_prob/kargerMinCut.txt

The file contains the adjacency list representation of a simple undirected
graph. There are 200 vertices labeled 1 to 200. The first column in the file
represents the vertex label, and the particular row (other entries except the
first column) tells all the vertices that the vertex is adjacent to.

So for example, the 6th row looks like : "6 155 56 52 120 ......".
This just means that the vertex with label 6 is adjacent to
(i.e., shares an edge with) the vertices with labels 155,56,52,120,...,etc

Your task is to code up and run the randomized contraction algorithm for the
min cut problem and use it on the above graph to compute the min cut
(i.e., the minimum-possible number of crossing edges)

(HINT: figure out an implementation of edge contractions. You might want to do
this naively, creating a new graph from the old every time there's an edge
contraction. Think about more efficient implementations.)

(WARNING: Make sure to run the algorithm many times with different random
seeds, and remember the smallest cut that you ever find.)

Educational notes:
 http://effbot.org/pyfaq/how-do-i-generate-random-numbers-in-python.htm
 http://www.python-course.eu/graphs_python.php
 http://shahriar.svbtle.com/underscores-in-python
 http://omar.toomuchcookies.net/node/2012/08/double-underscore-in-python-inheritance/
 https://wiki.python.org/moin/PythonDecoratorLibrary
 http://pythoncentral.io/validate-python-function-parameters-and-return-types-with-decorators/

'''

from copy import deepcopy
from random import choice as rchoice
from math import ceil, log
import matplotlib.pyplot as plt
import networkx as nx
import sys
import unittest


class ExtendedMultiGraph(nx.MultiGraph):
    """
    MultiGraph - graph class that allows multiple undirected edges between
    pairs of nodes.

    Using netwrokx module:
    -----
    >>> import networkx as nx
    >>> G=nx.Graph()
    >>> G.add_edge(1,2)
    >>> G.add_node(42)
    >>> print(sorted(G.nodes()))
    [1, 2, 42]
    >>> print(sorted(G.edges()))
    [(1, 2)]
    """

    def merge_nodes(self, v, u):
        for node in self[u]:
            self.add_edge(v, node)
        self.remove_node(u)
        self_loops = True
        while self_loops is True:
            try:
                self.remove_edge(v, v)
            except nx.NetworkXError:
                self_loops = False

    def rcontract_min_cut(self):
        """
        David Karger's '90s Random Contraction Algorithm

        -    While there are more than 2 vertices:
            i.    Pick a remaining edge (u,v) uniformly at random.
            ii.    Merge (or “contract”) u and v into a single vertex.
            iii.   Remove self-loops
        -    Return cut represented by final 2 vertices.
        """

        min_cut = 0
        tmp_graph = deepcopy(self)
        total_of_nodes = len(tmp_graph.nodes())

        # edge cases:
        if total_of_nodes in (0, 1):
            return min_cut

        # contraction loop (need to contract len-2 times to reach 2 nodes)
        for nodes_count in reversed(range(3, total_of_nodes+1)):
            # i. Pick a remaining edge (u,v) uniformly at random.
            v, u = rchoice(tmp_graph.edges())
            # ii. Merge (or “contract”) u and v into a single vertex.
            tmp_graph.merge_nodes(v, u)

        # result passing
        total_of_nodes = len(tmp_graph.nodes())
        if total_of_nodes is 2:
            return len(tmp_graph.edges())
        else:
            print("Error in rcontract_min_cut")
            return min_cut
        return min_cut

    def get_min_cut(self):
        min_cut = float('inf')
        len_nodes = len(self.nodes())

        # TODO: test repetition value + efficacy
        # Repetition = n^2*ln(n) -> p[fail]=1/n
        if len_nodes <= 10:
            REPETITION = 1000  # reduce chances of failure further than 1/n
        else:
            REPETITION = ceil((pow(len_nodes, 2)*log(len_nodes)))

        # run randomized contraction + save best min_cut result
        for _ in range(REPETITION):
            temp_min_cut = self.rcontract_min_cut()
            if temp_min_cut < min_cut:
                min_cut = temp_min_cut
        return min_cut

    @staticmethod
    def init_graph_wstrings(node_data_strings):
        """
        Initialize a new ExtendedMultiGraph:
        Accepts a list of strings, each holding information regarding
        a single node (first element) and its connections (separated by spaces)
        Returns a graph_object of type ExtendedMultiGraph(nx.MultiGraph)
        Holding node and edge information of the input data.
        """
        graph_object = ExtendedMultiGraph()
        for line in node_data_strings:
            assigned_node = False
            line_elements = list(map(int, line.split()))
            if line_elements[0] in graph_object.nodes():
                assigned_node = True
            else:
                graph_object.add_node(line_elements[0])
            for element_index in range(1, len(line_elements)):
                # if edge already listed, skip
                if (
                    # edge has been assigned by another
                    assigned_node and
                    # edge exists already
                    sorted((line_elements[0], line_elements[element_index])) in
                        sorted(graph_object.edges())):
                    continue
                # else add new edge
                (graph_object
                 .add_edge(line_elements[0], line_elements[element_index]))
        return graph_object


class ExtendedMultiGraphTestCase(unittest.TestCase):
    """Tests for `rcontract_min_cut.py`"""

    def test_networkx_module(self):
        my_graph = ExtendedMultiGraph()
        my_graph.add_edge(1, 2)
        my_graph.add_node(42)
        self.assertEqual(sorted(my_graph.nodes()), [1, 2, 42])
        self.assertEqual(sorted(my_graph.edges()), [(1, 2)])

    def test_init_graph_wstrings(self):
        adjacency_data = [
                          "1    4    3",
                          "2    3",
                          "3    1    2",
                          "4    1"
                          ]

        my_graph = ExtendedMultiGraph.init_graph_wstrings(adjacency_data)

        self.assertEqual(sorted(my_graph.nodes()), [1, 2, 3, 4])
        self.assertEqual(sorted(my_graph.edges()), [(1, 3), (1, 4), (2, 3)])

    def test_get_min_cut(self):

        my_graph1 = ExtendedMultiGraph()  # empty graph
        min_cut1 = my_graph1.get_min_cut()
        self.assertEqual(min_cut1, 0)

        my_graph2 = ExtendedMultiGraph()  # single node graph
        my_graph2.add_edge(1, 1)
        self.assertEqual(sorted(my_graph2.nodes()), [1])
        self.assertEqual(sorted(my_graph2.edges()), [(1, 1)])
        min_cut2 = my_graph2.get_min_cut()
        self.assertEqual(min_cut2, 0)

        my_graph3 = ExtendedMultiGraph()  # isolated node
        my_graph3.add_edge(1, 2)
        my_graph3.add_edge(1, 2)
        my_graph3.add_node(42)
        self.assertEqual(sorted(my_graph3.nodes()), [1, 2, 42])
        self.assertEqual(sorted(my_graph3.edges()), [(1, 2), (1, 2)])
        min_cut3 = my_graph3.get_min_cut()
        self.assertEqual(min_cut3, 0)

        my_graph3.remove_node(42)
        min_cut4 = my_graph3.get_min_cut()
        self.assertEqual(min_cut4, 2)

    def test_somthing(self):
        # TODO: implement some tests
        pass



def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # populate graph
        node_data_strings = [line.strip() for line in fh]
        my_graph = ExtendedMultiGraph.init_graph_wstrings(node_data_strings)

        if file_name[:4] == 'test':
            nx.draw_networkx(my_graph)
            plt.draw()
            plt.show()

        min_cut = my_graph.get_min_cut()

        print(min_cut)


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
