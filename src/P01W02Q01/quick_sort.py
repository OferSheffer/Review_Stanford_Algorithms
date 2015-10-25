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
from copy import deepcopy


class PivotMaker:
    pass


class PivotFirstElement(PivotMaker):
    """returns the first element index as the pivot"""

    def __init__(self, name="Question 1", pivoting_method="First Element"):
        self._name = name
        self._pivoting_method = pivoting_method

    def get_pivot(self, A, start, end):
        self._pivot = start
        return self._pivot


class PivotLastElement(PivotMaker):
    """returns the last element index as the pivot"""

    def __init__(self, name="Question 2", pivoting_method="Last Element"):
        self._name = name
        self._pivoting_method = pivoting_method

    def get_pivot(self, A, start, end):
        # TODO: get tge ubdex if the median and assign it to _pivot
        self._pivot = end-1
        return self._pivot


class PivotMedianElement(PivotMaker):
    """
    returns the median (from first, middle, last) element index as the pivot
    """

    def __init__(self, name="Question 3", pivoting_method="Median Element"):
        self._name = name
        self._pivoting_method = pivoting_method

    def get_pivot(self, A, start, end):
        n = end-start
        # mid_index:
        if n <= 2:
            self._pivot = start
            return self._pivot
        # else: n > 1:
        #     odd elements, e.g. 5 [0,1,2,3,4], mid_index=2 (n-1)/2
        #     even elements, e.g.4 [0,1,2,3], mid_index=1 (n-1)/2
        mid_index = start+(n-1)//2
        p_elements = [A[start], A[mid_index], A[end-1]]
        midean_value = sorted(p_elements)[1]

        # pivot=median index
        for i, p_element in enumerate(p_elements):
            if midean_value == p_element:
                self._pivot = [start, mid_index, end-1][i]
        return self._pivot


class PivotDirector():
    """Director"""
    def __init__(self, pivot_getter):
        self._pivot_getter = pivot_getter

    def get_pivot(self, *args):
        """
        get_pivot(A, start, end)
        Output: pivot_index
        """
        return self._pivot_getter.get_pivot(*args)

    def get_pivot_maker_data(self):
        return self._pivot_getter._name, self._pivot_getter._pivoting_method


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
        if A[j] <= pivot:    # if A[j] > p, do nothing
            swap(A, j, i)
            i += 1
    swap(A, start, i-1)
    return i-1


def quick_sort(A, start=0, end=None, pivot_director=None):
    # TODO: test different types of input for this arg setup
    """
    Input:
    array A, start(default=0), end(if default=None := len(A))
    pivot_director - used to get_pivot() via external factory method.
    Output: comparisons (# of times elements were compared during sorting)
    Side Effect: A is sorted.
    """
    if end is None:
        end = len(A)

    n = end - start
    if n <= 1:
        return 0    # base case, array of length 1 [or len(input)==0]
    else:
        # TODO:
        pivot_index = pivot_director.get_pivot(A, start, end)

        # first question: always choose pivot = 0 [first element]
        # pivot_index = start

        # Partition A around pivot, fix comparison count
        comparisons = n-1
#         # DEBUG
#         print(A, "\tpre-partition")
#         print("pivot: {}:'{}'".format(pivot_index,A[pivot_index]))
#         # END DEBUG
        
        pivot_index = partition(A, start, end, pivot_index)
        
#         # DEBUG
#         print(A, "\tpost-partition")
#         print("pivot: {}:'{}'\tcomp=\t{}".format(pivot_index,A[pivot_index],comparisons))
#         # END DEBUG

        # Input: 1st and 2nd partitions of current sub-array
        x = quick_sort(A, start, pivot_index, pivot_director)
        y = quick_sort(A, pivot_index+1, end, pivot_director)
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

        # TODO: more partition tests

    def test_quick_sort_with_basic_lists(self):
        """
        Are basic lists sorted correctly
        with output = # of comparisons?
        """

        # TODO: add assert tests for input types
        pf = PivotFirstElement()
        pd = PivotDirector(pf)

        A = []
        comp0 = quick_sort(A, pivot_director=pd)  # empty list input

        self.assertEqual(A, [])
        self.assertEqual(comp0, 0)

        A = [1]
        comp1 = quick_sort(A, pivot_director=pd)  # single element
        self.assertEqual(A, [1])
        self.assertEqual(comp1, 0)

        B = [1, 3, 5, 2, 4, 6]
        comp2 = quick_sort(B, pivot_director=pd)  # even length
        """
    '1' [1, 3, 5, 2, 4, 6]  - 5 comparisons
    '3'    [3, 5, 2, 4, 6]  - 4 comparisons
           [3, 2, 5, 4, 6]  - switch places
           [2, 3, 5, 4, 6]  - place pivot
    '2'    [2]              - 0 comparisons
    '5'          [5, 4, 6]  - 2 comparisons
                 [4, 5, 6]  - place pivot
                 [4]        - 0 comparisons
                       [6]  - 0 comparisons
                            - Total = 5+4+2=11
        """
        self.assertEqual(B, [1, 2, 3, 4, 5, 6])
        self.assertEqual(comp2, 11)  # expected comparisons for pivot = 1st

        C = [1, 3, 5, 2, 4, 6, 3]
        comp3 = quick_sort(C, pivot_director=pd)  # odd length, duplicate value
        """
    '1' [1, 3, 5, 2, 4, 6, 3]  - 6 comparisons
    '3'    [3, 5, 2, 4, 6, 3]  - 5 comparisons
    '3'    [3, 2, 3, 4, 6, 5]  - partitioned
    '3'    [3, 2]              - 1 comparison
    '4'             [4, 6, 5]  - 2 comparisons
    '6'                [6, 5]  - 1 comparisons
                               - Total = 6+5+1+2+1=15
        """
        self.assertEqual(C, [1, 2, 3, 3, 4, 5, 6])
        self.assertEqual(comp3, 15)  # expected comparisons for pivot = 1st

        # TODO: implement testing for all pivot types.
        # TODO: add pivot factory to tests

    def test_pivot_median_element(self):
        pf = PivotMedianElement()
        pd = PivotDirector(pf)

        A = []    # empty list input
        comp0 = quick_sort(A, pivot_director=pd)

        self.assertEqual(A, [])
        self.assertEqual(comp0, 0)

        A = [1]    # single element
        comp1 = quick_sort(A, pivot_director=pd)
        self.assertEqual(A, [1])
        self.assertEqual(comp1, 0)

        B = [1, 3, 5, 2, 4, 6]    # even length
        comp2 = quick_sort(B, pivot_director=pd)
        """
        [1, 3, 5, 2, 4, 6]  - 1,5,6->'5'
    '5' [5, 3, 1, 2, 4, 6]  - 5 comparisons
        [4, 3, 1, 2, 5, 6]  - done
        [4, 3, 1, 2]        - 4,3,2->'3'
    '3' [3, 4, 1, 2]        - 3 comparisons
    '3' [2, 1, 3, 4]        - done
    '1' [2, 1]              - 1 comparison
                            - Total = 5+3+1=9
        """
        self.assertEqual(B, [1, 2, 3, 4, 5, 6])
        self.assertEqual(comp2, 9)  # expected comparisons for pivot = 1st


def main(file_name):
    # take values from file and run quick_sort
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file
        o_data = list(map(int, [line.strip() for line in fh]))

        # populate a dict with all possible PivotMakers
#         m = sys.modules[__name__]
#         pivot_factories = {}
#         for module_attribute_name in dir(m):
#             module_attribute = getattr(m, module_attribute_name)
#             if inspect.isclass(module_attribute) and
#                 issubclass(module_attribute, PivotMaker) and
#                 module_attribute != PivotMaker:
#                 pivot_factories[module_attribute.name] = module_attribute

        pivot_factories = dict(
                          # q1=PivotFirstElement(),
                          # q2=PivotLastElement(),
                          q3=PivotMedianElement()
                          )

        for _, pf in sorted(pivot_factories.items()):
            A = deepcopy(o_data)
            pd = PivotDirector(pf)
            print("{1}, Pivoting Method: {2}, Comparisons: {0}".format(
                            quick_sort(A, pivot_director=pd),
                            *(pd.get_pivot_maker_data()))
                  )


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
