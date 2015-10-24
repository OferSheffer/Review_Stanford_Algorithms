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

import unittest
import sys
# TODO: if debug import unittest

# TODO: create pivot_factory method


def quick_sort(A, length, pivot_factory=None):
    """
    Input: 
    array A, length n,      ??start_index(default=0)?? (consider)
    pivot_factory - used to get_pivot() via external factory method.
    Output: comparisons (# of times elements were compared during sorting)
    Side Effect: A is sorted.
    """
    if n <= 1:
        return 0    # base case, array of length 1 [or len(input)==0]
    else:
        p = pivot_factory.choose_pivot(A, length)

        # TODO: Partition A around p, fix comparison count

        # Input: 1st and 2nd partitions of current sub-array
        x = quick_sort(A, len_1st, start_index, pivot_factory=None)
        y = quick_sort(A, len_1st, start_index, pivot_factory=None)
    return x+y


class Test_quick_sort(unittest.TestCase):
    """
    Basic test class
    """

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


def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print(fh.readline())  # remove first answer line from debug file
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
