'''
Created on Oct 24, 2015
@author: Ofer

Question 1
Download the text file here. (Right click and save link as)
http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt

GENERAL DIRECTIONS
The file contains all of the integers between 1 and 10,000 (inclusive, with no
repeats) in unsorted order. Compute the total number of comparisons used to
sort the given input file by QuickSort.

Don’t count comparisons one-by-one. Rather, upon a recursive call on a subarray
of length m, simply add m−1 to running total of comparisons.
(Pivot compared to each of the other m−1 elements in this call's subarray.)

Explore three different pivoting rules:
Question 1: Always use the first element of the array as the pivot element.
    WARNING: Implement the Partition subroutine exactly as described in the
    video lectures.
Question 2: Always use the final element of given arrays as the pivot element.
    Recall from the lectures that, just before the main Partition subroutine,
    you should exchange the pivot element (i.e., the last element) with the
    first element.
Question 3: Use the "median-of-three" pivot rule.
    [Extra work = much better performance with nearly sorted/reversed input.]

    Note: Even length array 2k, use the kth element as the "middle" element.
    E.g. array 4 5 6 7, "middle" element is the second one ---- 5 and not 6!

    Identify median between 1st, middle, last and use this as your pivot.
    Exchange pivot with first element just before main Partition subroutine.

    EXAMPLE: Input array 8 2 4 5 7 1 - first (8), middle (4), and last (1)
    since 4 is the median of the set {1,4,8}, you would use 4 as your pivot.
    SUBTLE POINT: Don't include comparisons from median selection analysis.


Educational Notes:
 Concatenating immutable sequences always results in a new object. This means
 that building up a sequence by repeated concatenation will have a quadratic
 runtime cost in the total sequence length - e.g. like the question about
 repeated merge-sorts on k sequences of length n. To get a linear runtime
 cost see:  https://docs.python.org/3/library/stdtypes.html

Python TimeComplexity:
 https://wiki.python.org/moin/TimeComplexity

'''

import sys
import unittest

# TODO: create pivot_factory method


def swap(A, index_1, index_2):
    """swap between two members of array A"""
    if index_1 == index_2:
        return
    # else: index_1 != index_2
    temp = A[index_2]
    A[index_2] = A[index_1]
    A[index_1] = temp


def partition(A, start, end, pivot_index):
    """
    Input: array A[start:end]
    Output: index of pivot once partition is complete
    Side effect:
        A[start:end] is divided into:
        "smaller than pivot","pivot","larger than pivot"
    """
    if end-start < 0:
        raise ValueError
    if not (start <= pivot_index <= end):
        raise ValueError

    # subarray with single or no elements
    if end-start <= 1:
        return start

    # else: subarray with more than 1 element
    # place pivot element at the start
    swap(A, start, pivot_index)
    pivot = A[start]

    # partition (iterate over j, bucket 'smaller'/'larger'-than-pivot values)
    i = start+1
    for j in range(start+1, end):
        if A[j] < pivot:    # if A[j] > p, do nothing
            swap(A, j, i)
            i += 1
    swap(A, start, i-1)
    return i-1


def quick_sort(A, start=0, end=None, pivot_factory=None):
    # TODO: test different types of input for this arg setup
    """
    Input:
    array A, length n,      ??start_index(default=0)?? (consider)
    pivot_factory - used to get_pivot() via external factory method.
    Output: comparisons (# of times elements were compared during sorting)
    Side Effect: A is sorted.
    """
    if not end:
        end = len(A)

    n = end - start
    if n <= 1:
        return 0    # base case, array of length 1 [or len(input)==0]
    else:
        # TODO:
        # pivot_index = pivot_factory.get_pivot(A, start, end)

        # first question: always choose pivot = 0 [first element]
        pivot_index = 0

        # Partition A around pivot, fix comparison count
        comparisons = n-1
        pivot_index = partition(A, start, end, pivot_index)

        # Input: 1st and 2nd partitions of current sub-array
        x = quick_sort(A, start, pivot_index, pivot_factory)
        y = quick_sort(A, pivot_index+1, end, pivot_factory)
    return comparisons+x+y


class QuickSortTestCase(unittest.TestCase):
    """Tests for `quick_sort.py`"""

    def test_swap(self):
        A = [2, 3]
        swap(A, 0, 1)
        self.assertEqual(A, [3, 2])

    def test_partition(self):
        A = []
        pivot_index = partition(A, 0, 0, 0)
        self.assertEqual(A, [])
        self.assertEqual(pivot_index, 0)

        B = [3, 5, 2, 1, 4]
        pivot_index = partition(B, 0, 5, 2)

        """
        [3, 5, 2, 1, 4] - original input array
        [2, 5, 3, 1, 4] - swap pivot with first
        [2, 5, 3, 1, 4] - compare first with 5, and then with 3 (no change)
        [2, 1, 3, 5, 4] - swap pos[1] with '1', advance index to 2
        [2, 1, 3, 5, 4] - compare first with 4 (no change)
        [1, 2, 3, 5, 4] - swap pos[0] with index-1, return index-1=1
        """
        self.assertEqual(B, [1, 2, 3, 5, 4])
        self.assertEqual(pivot_index, 1)

        # TODO: make more tests

    def test_quick_sort_with_basic_lists(self):
        """
        Are basic lists sorted correctly
        with output = # of comparisons?
        """

        # TODO:
        return

        # TODO: fix basic test with proper assert values
        A = []
        comp0 = quick_sort(A, len(A))  # empty list input

        self.assertEqual(A, [])
        self.assertEqual(comp0, 0)

        A = [1]
        comp1 = quick_sort(A, len(A))  # single element
        self.assertEqual(A, [1])
        self.assertEqual(comp1, 0)

        B = [1, 3, 5, 2, 4, 6]
        comp2 = quick_sort(B,  len(B))  # even length
        self.assertEqual(B, [1, 2, 3, 4, 5, 6])
        self.assertEqual(comp2, 3)  # expected comparisons for pivot = 1st

        C = [1, 3, 5, 2, 4, 6, 3]
        comp3 = quick_sort(C, len(C))  # odd length, duplicate value
        self.assertEqual(C, [1, 2, 3, 3, 4, 5, 6])
        self.assertEqual(comp3, 6)

    def test_with_pivots(self):
        # TODO: implement testing for all pivot types.
        # TODO: add pivot factory to tests
        pass


def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file
        A = list(map(int, [line.strip() for line in fh]))
        print(quick_sort(A, len(A)))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
