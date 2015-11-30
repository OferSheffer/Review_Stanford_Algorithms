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
numbers x,y (x != y) in the input file that satisfy x+y=t.
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
# from multiprocessing import Pool

MIN_RANGE = -10000
MAX_RANGE = 10000
_SORTED_ARRAY = False
_SORTED_ARRAY = True


class ExtendedSet(set):
    def twosum(self, t):
        """
        evaluates if distinct x,y (x != y) exist that make x+y=t
        returns 1 if true, else 0"""
        for x in self:
            c = t-x
            if (c in self) and (c != x):
                return 1
        return 0


def ranged_twosum(my_sorted_data, MIN_RANGE, MAX_RANGE):
    """
    evaluates if distinct x,y (x != y) exist that make x+y=t
    returns 1 if true, else 0
    """
    counter = 0
    direction = -1
    j = len(len(my_sorted_data)-1)
    y = my_sorted_data[j]
    for i in range(0, len(my_sorted_data)-1):
        if i % 500 == 0:
            print("i index: {}, counter: {}".format(i, counter))
        x = my_sorted_data[i]
        if x > MAX_RANGE:
            break

        if direction == -1:
            j = end_pos
            while y + x >= MIN_RANGE:
                y = my_sorted_data[j]

                if x + y <= MAX_RANGE:
                    counter += 1
                
                j
                    
                    
                    
        
        
        
        
        
        
#         if x < 0:
#             for j in range(len(my_sorted_data)-1, i, -1):
#                 y = my_sorted_data[j]
#                 if y + x < MIN_RANGE or x == y:
#                     break
#                 elif x + y <= MAX_RANGE:
#                     counter += 1
#         else:  # x >= 0
#             if x > MAX_RANGE:
#                 break
#             for j in range(i+1, len(my_sorted_data)):
#                 y = my_sorted_data[j]
#                 if y + x > MAX_RANGE or x == y:
#                     break
#                 elif x + y <= MAX_RANGE:
#                     counter += 1
    return counter


class TwoSumTestCase(unittest.TestCase):
    """Tests for `twosum.py`"""

    def test_data_hashing(self):
        """init data"""
        test_input = "-10"+"\n" \
                     "-20"+"\n" \
                     "30"+"\n"  \
                     "21"+"\n" \
                     "15"+"\n" \
                     "30"

        my_hashed_data = set()
        for num in map(int, test_input.split('\n')):
            my_hashed_data.add(num)

        self.assertEqual(my_hashed_data, {-10, -20, 30, 21, 15})

    def test_twosum(self):
        """init data"""
        test_input = "-12"+"\n" \
                     "-20"+"\n" \
                     "5"+"\n" \
                     "30"+"\n"  \
                     "21"+"\n" \
                     "15"+"\n" \
                     "30"

        my_hashed_data = ExtendedSet()
        for num in map(int, test_input.split('\n')):
            my_hashed_data.add(num)

        self.assertEqual(my_hashed_data.twosum(9), 1)
        self.assertEqual(my_hashed_data.twosum(51), 1)
        self.assertEqual(my_hashed_data.twosum(12), 0)
        self.assertEqual(my_hashed_data.twosum(5), 0,
                         msg="set: {}".format(my_hashed_data))

        my_hashed_data.add(0)
        self.assertEqual(my_hashed_data.twosum(5), 1)





def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        if not _SORTED_ARRAY:
            # populate hash table
            my_hashed_data = ExtendedSet()
            for line in fh:
                my_hashed_data.add(int(line.strip()))

        # alternatively, populate a sorted array
        if _SORTED_ARRAY:
            my_hashed_data = set()
            for line in fh:
                my_hashed_data.add(int(line.strip()))
            my_sorted_data = list(my_hashed_data)
            my_sorted_data = sorted(my_sorted_data)  # makes things faster for repeated 2-SUMs
            print("sorted")

        # suggested threaded solution - still slow for hashed data
#         t = [x for x in range(-10000, 10001)]
#         pool = Pool(8)
#         result = pool.map(my_hashed_data.twosum, t)
#         # pool.join()
#         print (sum(result))

        xy_pairs = 0
        if not _SORTED_ARRAY:
            for t in range(MIN_RANGE, MAX_RANGE+1):
                if t % 1000 is 0:
                    print("t={}, xy_pairs={}".format(t, xy_pairs))
                xy_pairs += my_hashed_data.twosum(t)

        # alternatively, work with a sorted array
        if _SORTED_ARRAY:
            xy_pairs += ranged_twosum(my_sorted_data, MIN_RANGE, MAX_RANGE)

        print("Number of distinct x,y pairs: {}".format(xy_pairs))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
