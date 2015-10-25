'''
Created on Oct 24, 2015
@author: Ofer

Testing for quick_sort module

Reminder - quicksort() returns a counter for the number of comparisons
'''

import unittest
from quick_sort import partition, quick_sort


class QuickSortTestCase(unittest.TestCase):
    """Tests for `quick_sort.py`"""

    def test_quick_sort_with_basic_lists(self):
        """
        Are basic lists sorted correctly
        with output = # of comparisons?
        """

        # TODO: fix basic test with proper assert values
        A = []
        res0 = quick_sort(A, len(A))  # empty list input

        self.assertEqual(A, [])
        self.assertEqual(res0, 0)

        A = [1]
        res1 = quick_sort(A, len(A))  # single element
        self.assertEqual(A, [1])
        self.assertEqual(res1, 0)

        B = [1, 3, 5, 2, 4, 6]
        res2 = quick_sort(B,  len(B))  # even length
        self.assertEqual(B, [1, 2, 3, 4, 5, 6])
        self.assertEqual(res2, 3)

        C = [1, 3, 5, 2, 4, 6, 3]
        res3 = quick_sort(C, len(C))  # odd length, duplicate value
        self.assertEqual(C, [1, 2, 3, 3, 4, 5, 6])
        self.assertEqual(res3, 6)

    def test_with_pivots(self):
        # TODO: implement testing for all pivot types.
        # TODO: add pivot factory to tests
        pass
    
if __name__ == '__main__':
    unittest.main()
