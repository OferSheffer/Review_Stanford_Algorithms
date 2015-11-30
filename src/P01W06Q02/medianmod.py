'''
Created on Nov 30, 2015

@author: Ofer

Download the text file here.
http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt

Implement the "Median Maintenance" algorithm
(Week 5 lecture on heap applications).

The text file contains a list of the integers from 1 to 10000 in unsorted
order; you should treat this as a stream of numbers, arriving one by one.

Letting xi denote the ith number of the file, the kth median mk is defined as
the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th
smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest
number among x1,…,xk.)

Find the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). I.e., compute (m1+m2+m3+⋯+m10000) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.



IMPLEMENTATION NOTES:

'''

import sys
import unittest


class MedianModTestCase(unittest.TestCase):
    """Tests for `twosum.py`"""

    def test_median(self):
        """init data"""
        pass
        # self.assertEqual(my_hashed_data, {-10, -20, 30, 21, 15})


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        result = 0
        data = []
        for line in fh:
            new_value = int(line.strip())
            result += streamed_median(data, new_value)

        print("Number of distinct x,y pairs: {}".format(result))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
