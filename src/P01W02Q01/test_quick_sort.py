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

    def test_quick_sort(self):
        # TODO: fix basic test with proper assert values
        # TODO: add pivot factory to tests
        A = []
        res0 = quick_sort(A, len(A))  # empty list input
        self.assertEqual(res0, 0)
        A = [1]
        res1 = quick_sort(A, len(A))  # single element
        self.assertEqual(res1, 0)
        B = [1, 3, 5, 2, 4, 6]
        res2 = quick_sort(B,  len(B))  # even length
        self.assertEqual(res2, 3)
        C = [1, 3, 5, 2, 4, 6, 3]
        res3 = quick_sort(C, len(C))  # odd length, duplicate value
        self.assertEqual(res3, 6)

    def test_with_pivots(self):
        # TODO: implement testing for all pivot types.
        pass
    
if __name__ == '__main__':
    unittest.main()
