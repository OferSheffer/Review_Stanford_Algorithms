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

Thoughts:
 1. Considering row 8 has vertex no. 8, is it necessary to make a data
    structure for the vertices?
    - keeping vertices as a list, deletion is 'different'.
 2. is there an existing Graph class that I can use and just add to the
    exiting API?
'''

from random import randrange
import networkx as nx
import sys
import unittest

# from graph import Graph


REPETITION = 200  # n^n*ln(n)

irand = randrange(0, 10)


class Extended_Graph(nx.Graph):
    """
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
    def rcontract_min_cut(self):
        """
        David Karger's Random Contraction Algorithm

        -    While there are more than 2 vertices:
        i.    Pick a remaining edge (u,v) uniformly at random.
        ii.    Merge (or “contract”) u and v into a single vertex.
        iii.    Remove self-loops
        iv.    Return cut represented by final 2 vertices.
        """

        # TODO: create this algorithm
        return 0
        pass

    def get_min_cut(self):
        min_cut = None
        for _ in range(REPETITION):
            temp_min_cut = rcontract_min_cut(graph)
            if temp_min_cut < min_cut:
                min_cut = temp_min_cut
        return min_cut

    @property
    def set_graph_data(adjacency_data):
        # TODO: implement
        for line in adjacency_data:
            items = [map(int, line.split())]

            # if set (items[0],item_i).sorted() not in edge_set
            # add this edge to the edge_set

        return "", ""


class ExtendedGraphTestCase(unittest.TestCase):
    """Tests for `rcontract_min_cut.py`"""

    def test_networkx_module(self):
        my_graph = Extended_Graph()
        my_graph.add_edge(1, 2)
        my_graph.add_node(42)
        self.assertEqual(sorted(my_graph.nodes()), [1, 2, 42])
        self.assertEqual(sorted(my_graph.edges()), [(1, 2)])

    def test_initialize_graph_data(self):
        adjacency_data = [
                          "1    4    3",
                          "2    3",
                          "3    1,    2",
                          "4    1"
                          ]

        self.assertTrue(graph.keys().sorted() == [1, 2, 3, 4],
                        "Not yet implemented.")
        self.assertTrue(graph.get_edges().sorted() == [(1, 3), (1, 4), (2, 3)],
                        "Not yet implemented.")

    def test_somthing(self):
        # TODO: implement some tests
        pass


def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # populate graph
        my_graph = Extended_Graph()
        node_data_strings = [line.strip() for line in fh]
        for node_string in node_data_strings:
            get_graph_data(adjacency_data)
 
        min_cut = get_min_cut(v_data, e_data)

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
