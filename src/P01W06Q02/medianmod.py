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

import heapq
import sys
import unittest


class StreamedMedian(object):
    """
    Heaps:
    H_low: supports extract Max [get biggest of the smaller numbers]
    H_high: supports extract Min
    """
    def __init__(self):
        self._left = []   # TODO: test max heap
        self._right = []  # TODO: test min_heap
        self._offset = 0  # len(right) - len(left)
        self._median = None

    def add_value(self, new_value):
        if not self.median:
            self.median = new_value
            self.addleft(new_value)
        # else:
        elif self._offset == 0:  # even lengths
            if new_value <= self.minright:
                self.addleft(new_value)
                if new_value > self.median:
                    self.median = new_value
            else:
                self.addleft(self.pushpopright(new_value))
                self.median = self.maxleft

        elif self._offset == -1:  # left side bigger by 1
            if new_value < self.median:
                self.addright(self.pushpopleft(new_value))
                self.median = self.maxleft
            else:
                self.addright(new_value)
        else:
            print("offset error")
            sys.exit()

    def addleft(self, val):
        heapq.heappush(self._left, val)
        heapq._heapify_max(self._left)
        self._offset -= 1

    def addright(self, val):
        heapq.heappush(self._right, val)
        self._offset += 1

    def pushpopleft(self, val):
        # self._offset += 1
        return heapq._heappushpop_max(self._left, val)

    def pushpopright(self, val):
        # self._offset -= 1
        return heapq.heappushpop(self._right, val)

    @property
    def maxleft(self):
        return self._left[0]

    @property
    def minright(self):
        return self._right[0]

    @property
    def median(self):
        return self._median

    @median.setter
    def median(self, val):
        self._median = val

    def __len__(self):
        return len(self._left) + len(self._right)

    def __str__(self):
        d = heapq.nsmallest(len(self._left), self._left)
        if len(self._right) > 0:
            d.extend(heapq.nsmallest(len(self._right), self._right))
        return repr(d)


class MedianModTestCase(unittest.TestCase):
    """Tests for `twosum.py`"""

    def test_median(self):
        """init data"""
        data = StreamedMedian()
        medians = []
        new_value = 4
        data.add_value(new_value)
        medians.append(data.median)
        self.assertEqual(str(data), '[4]')
        self.assertEqual(medians, [4])

        new_value = 6
        data.add_value(new_value)
        medians.append(data.median)
        self.assertEqual(str(data), '[4, 6]')
        self.assertEqual(medians, [4, 4])

        new_value = 7
        data.add_value(new_value)
        medians.append(data.median)
        self.assertEqual(str(data), '[4, 6, 7]')
        self.assertEqual(medians, [4, 4, 6])

        new_values = [10, 5, 2, 4, 8, -1, 0]
        for val in new_values:
            data.add_value(val)
            medians.append(data.median)
        self.assertEqual(str(data), '[-1, 0, 2, 4, 4, 5, 6, 7, 8, 10]')
        """
        '[4, 6, 7]'--10-->'[4, 6, 7, 10]'--5-->'[4, 5, 6, 7, 10]'
        --2-->'[2, 4, 5, 6, 7, 10]'--4-->'[2, 4, 4, 5, 6, 7, 10]'
        --8-->'[2, 4, 4, 5, 6, 7, 8, 10]'--1-->'[-1, 2, 4, 4, 5, 6, 7, 8, 10]'
        --0-->'[-1, 0, 2, 4, 4, 5, 6, 7, 8, 10]'
        """
        self.assertEqual(medians, [4, 4, 6, 6, 6, 5, 5, 5, 5, 4])


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        medians = []

        data = StreamedMedian()
        for line in fh:
            new_value = int(line.strip())
            data.add_value(new_value)
            medians.append(data.median)

        result = sum(medians) % 10000

        print("sum(medians) % 10000: {}".format(result))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
