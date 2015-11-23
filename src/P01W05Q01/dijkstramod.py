'''
Created on Nov 23, 2015

@author: Ofer

In this programming problem you'll code up Dijkstra's shortest-path algorithm.
Download the text file here. (Right click and save link as).
http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt

The file contains an adjacency list representation of an undirected weighted
graph with 200 vertices labeled 1 to 200. Each row consists of the node tuples
that are adjacent to that particular vertex along with the length of that edge.
For example, the 6th row has 6 as the first entry indicating that this row
corresponds to the vertex labeled 6. The next entry of this row "141,8200"
indicates that there is an edge between vertex 6 and vertex 141 that has length
8200. The rest of the pairs of this row indicate the other vertices adjacent to
vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1
(the first vertex) as the source vertex, and to compute the shortest-path
distances between 1 and every other vertex of the graph. If there is no path
between a vertex v and vertex 1, we'll define the shortest-path distance
between 1 and v to be 1000000.

You should report the shortest-path distances to the following ten vertices,
in order: 7,37,59,82,99,115,133,165,188,197. You should encode the distances
as a comma-separated string of integers. So if you find that all ten of these
vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000
distance away, then your answer should be
1000,1000,1000,1000,1000,2000,1000,1000,1000,1000.
Remember the order of reporting DOES MATTER, and the string should be in the
same order in which the above ten vertices are given.

IMPLEMENTATION NOTES:
This graph is small enough that the straightforward O(mn) time implementation
of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking
an additional challenge, try implementing the heap-based version. Note this
requires a heap that supports deletions, and you'll probably need to maintain
some kind of mapping between vertices and their positions in the heap.
'''

import networkx as nx
import sys
import unittest

MAXDISTANCE = 1000000


class ExtendedGraph(nx.Graph):
    """
    Graph - graph class that implements an undirected graph.
    It ignores multiple edges between two nodes.
    It does allow self-loop edges between a node and itself.

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

    @staticmethod
    def translate_data(line):
        split = line.split(maxsplit=1)
        node = int(split[0])
        node_connections_strings = split[1].split()
        for i, str_ in enumerate(node_connections_strings):
            node_connections_strings[i] = tuple(map(int, str_.split(",")))
        return node, node_connections_strings

    @staticmethod
    def init_weightedgraph_wstrings(node_data_strings):
        """
        Initialize a new ExtendedGraph:
        Accepts a list of strings, each holding information regarding
        a single node (first element)
        and its weighted connections (tuples, separated by spaces)
        Returns a graph_object of type ExtendedGraph(nx.Graph)
        Holding node, edge and weight information of the input data.
        """
        graph_object = ExtendedGraph()
        # TODO: check that there is no duplicates
        for line in node_data_strings:
            node, node_connections = ExtendedGraph.translate_data(line)
            for connection in node_connections:
                graph_object.add_edge(node, connection[0],
                                      weight=connection[1])
        return graph_object


class ExtendedGraphTestCase(unittest.TestCase):
    """Tests for `rcontract_min_cut.py`"""

    def test_networkx_module(self):
        my_graph = ExtendedGraph()
        my_graph.add_edge(1, 2, weight=4.7)
        my_graph.add_node(42)
        self.assertEqual(sorted(my_graph.nodes()), [1, 2, 42])
        self.assertEqual(sorted(my_graph.edges()), [(1, 2)])
        self.assertEqual(
                         list(nx.generate_edgelist(my_graph)),
                         ["1 2 {'weight': 4.7}"])

    def test_init_weightedgraph_wstrings(self):
        adjacency_data = [
                          "1    4,10    3,20",
                          "2    3,50",
                          "3    1,20    2,50",
                          "4    1,10"
                          ]

        my_graph = ExtendedGraph.init_weightedgraph_wstrings(adjacency_data)

        self.assertEqual(sorted(my_graph.nodes()), [1, 2, 3, 4])
        self.assertEqual(sorted(my_graph.edges()), [(1, 3), (1, 4), (2, 3)])
        self.assertEqual(
                         list(nx.generate_edgelist(my_graph)),
                         ["1 3 {'weight': 20}",
                          "1 4 {'weight': 10}",
                          "2 3 {'weight': 50}"])


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # populate graph
        node_data_strings = [line.strip() for line in fh]
        my_graph = ExtendedGraph.init_weightedgraph_wstrings(node_data_strings)

        topfive = my_graph.topfive_scc_sizes()

        print(topfive)


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
