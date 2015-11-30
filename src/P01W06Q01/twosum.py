'''
Created on Nov 30, 2015

@author: Ofer

Download the text file here. (Right click and save link as).
https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt

The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative
(there might be some repetitions!). This is your array of integers,
with the ith row of the file specifying the ith entry of the array.
Your task is to compute the number of target values t
in the interval [-10000,10000] (inclusive) such that there are distinct
numbers x,y in the input file that satisfy x+y=t.
(NOTE: ensuring distinctness requires a one-line
 addition to the algorithm from lecture.)

Your numeric answer should be an integer between 0 and 20001.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing
your own hash table for it. For example, you could compare performance under
the chaining and open addressing approaches to resolving collisions.


IMPLEMENTATION NOTES:

'''

import sys
import unittest


class TwoSumTestCase(unittest.TestCase):
    """Tests for `twosum.py`"""

    def test_something(self):
        """init data"""
        """self.assertEqual(operation, expected output)"""
        raise NotImplementedError


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # TODO: populate hash table
        my_hashed_data = [line.strip() for line in fh]
        xy_pairs = my_hashed_data.get_twosum(t)  # return x,y where x+y=t

        print("Number of distinct x,y pairs: {}".format(len(xy_pairs)))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
