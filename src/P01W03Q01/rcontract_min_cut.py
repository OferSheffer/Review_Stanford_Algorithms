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
import copy
import sys
import unittest

REPETITION = 200  # n^n*ln(n)

irand = randrange(0, 10)


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


def rcontract_min_cut(graph):
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


def get_min_cut(graph):
    min_cut = None
    for _ in range(REPETITION):
        temp_min_cut = rcontract_min_cut(graph)
        if temp_min_cut < min_cut:
            min_cut = temp_min_cut
    return min_cut


def get_graph_data(adjacency_data):
    # TODO: implement
    for line in adjacency_data:
        items = [map(int, line.split())]

        # if set (items[0],item_i).sorted() not in edge_set
        # add this edge to the edge_set

    return "", ""


class QuickSortTestCase(unittest.TestCase):
    """Tests for `rcontract_min_cut.py`"""

    def test_initialize_graph_data(self):
        adjacency_data = [
                          "1    4    3",
                          "2    3",
                          "3    1,    2",
                          "4    1"
                          ]
        graph = get_graph_data(adjacency_data)

        self.assertTrue(graph.keys().sorted() == [1, 2, 3, 4],
                        "Not yet implemented.")
        self.assertTrue(graph.get_edges().sorted() == [(1, 3), (1, 4), (2, 3)],
                        "Not yet implemented.")

    def test_somthing(self):
        self.assertTrue(None, "Not yet implemented.")
        # TODO: implement some tests
        pass

    def test_somthing(self):
        # TODO: implement some tests
        pass


def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file
        adjacency_data = [line.strip() for line in fh]
        for line in adjacency_data:
            v_data, e_data = get_graph_data(adjacency_data)

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
