'''
Created on Nov 15, 2015

@author: Ofer
'''
import sys
import unittest


class SccMod(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # populate graph
        node_data_strings = [line.strip() for line in fh]
        # TODO: replace Extended with new data structure
        # TODO: new init_graph_wstrings() method
        my_graph = ExtendedMultiGraph.init_graph_wstrings(node_data_strings)

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