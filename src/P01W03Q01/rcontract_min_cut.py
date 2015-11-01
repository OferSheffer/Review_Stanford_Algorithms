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

(HINT: Note that you'll have to figure out an implementation of edge
contractions. Initially, you might want to do this naively, creating a new
graph from the old every time there's an edge contraction. But you should
also think about more efficient implementations.)

(WARNING: As per the video lectures, please make sure to run the algorithm
many times with different random seeds, and remember the smallest cut that
you ever find.)

Educational notes:
 http://effbot.org/pyfaq/how-do-i-generate-random-numbers-in-python.htm

'''

from random import randrange
import sys
import unittest

REPETITION = 200  # n^n*ln(n)

irand = randrange(0, 10)


def rcontract_min_cut(o_data):
    # TODO: create this algorithm
    return 0
    pass


def get_min_cut(v_data, e_data):
    min_cut = None
    for _ in range(REPETITION):
        min_cut = rcontract_min_cut(v_data, e_data)
    return min_cut


def get_graph_data(adjacency_data):
    # TODO: implement
    return "", ""


class QuickSortTestCase(unittest.TestCase):
    """Tests for `rcontract_min_cut.py`"""

    def test_get_graph_data(self):
        adjacency_data = [
                          "1    4    3",
                          "2    3",
                          "3    1,    2",
                          "4    1"
                          ]
        v_data, e_data = get_graph_data(adjacency_data)

        self.assertTrue(v_data.keys().sorted() == [1, 2, 3, 4],
                        "Not yet implemented.")
        self.assertTrue(e_data.values().sorted() == [(1, 3), (1, 4), (2, 3)],
                        "Not yet implemented.")
        self.assertTrue(None, "Not yet implemented.")

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
