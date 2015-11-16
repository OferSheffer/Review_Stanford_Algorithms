'''
Created on Nov 15, 2015

@author: Ofer

Question 1
Download the text file here. (Right click and save link as)
http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.txt
Zipped version here.
http://spark-public.s3.amazonaws.com/algo1/programming_prob/SCC.zip

The file contains the edges of a directed graph. Vertices are labeled as
positive integers from 1 to 875714. Every row indicates an edge, the vertex
label in first column is the tail and the vertex label in second column is the
head (recall the graph is directed, and the edges are directed from the first
column vertex to the second column vertex). So for example, the 11th row looks
liks : "2 47646". This just means that the vertex with label 2 has an outgoing
edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing
strongly connected components (SCCs), and to run this algorithm on the given
graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given
graph, in decreasing order of sizes, separated by commas (avoid any spaces).
So if your algorithm computes the sizes of the five largest SCCs to be
500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100".
If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms.
Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0".

WARNING:
Because of the size of the graph you may have to manage memory carefully.

Educational notes:
 http://codereview.stackexchange.com/questions/109749/random-contraction-min-cut-karger-performance-issues
 I would try networkx digraph, but getting poor results with nx.MultiGraph on
 karger's min cut algorithm (Week 03) and being low on time, I'll implement
 my own class and look for fast-working graph modules at a later date.

 Don't use non-hashable types as keys. Silly.
'''


import sys
import unittest

from P01W04Q01 import mygraphmodule as mgm


class SccMod(mgm.MyDiGraph):
    '''
    An implementation of MyDiGraph module
    extended with an SCC related algorithm

    >>> G=mgm.Graph()
    >>> G.add_arc(1,2)
    >>> G.add_node(42)
    >>> print(sorted(G.nodes()))
    [1, 2, 42]
    >>> print(sorted(G.arcsedges()))
    [(1, 2)]
    '''

    def __init__(self):
        super().__init__()

    @staticmethod
    def init_graph_warcstrings(node_arcs_strings):
        """
        Initialize a new SccMod:
        Accepts a list of strings, each holding information regarding
        a single arc (two nodes separated by spaces)
        Returns a graph_object of type SccMod(mgm.MyDiGraph)
        Holding adjacency representation of the graph.
        """
        graph_object = SccMod()
        for line in node_arcs_strings:
            arc_elements = mgm.Arc(*list(map(
                                             mgm.Node.strint_to_node,
                                             line.split()
                                             )
                                         ))
            graph_object.add_arc(arc_elements)
        return graph_object


class SccModTestCase(unittest.TestCase):
    """Tests for `sccmod.py`"""
    def test_init_graph_wstrings(self):
        node_arcs_strings = [
                             "1 4",
                             "1 3",
                             "2 3"
                             ]

        my_graph = SccMod.init_graph_warcstrings(node_arcs_strings)

        self.assertEqual(sorted(list(my_graph.nodes)), [1, 2, 3, 4])
        self.assertEqual(sorted(list(my_graph.arcs)), [(1, 3), (1, 4), (2, 3)])


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # populate graph
        node_arcs_strings = [line.strip() for line in fh]
        # TODO: init_graph_wstrings() method for SccMod
        # my_graph = ExtendedMultiGraph.init_graph_wstrings(node_data_strings)
        my_graph = SccMod.init_graph_warcstrings(node_arcs_strings)

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
