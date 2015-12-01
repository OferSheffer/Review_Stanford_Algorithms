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
Basic hash based implementation is O(k*n) with k = 20000 and n = 10E6
runtime is considerable. Multithreading eased it off a bit, but it is
not great still.

A sorted array based implementation can have a much smaller constant.

'''

import sys
import unittest
# from multiprocessing import Pool

MIN_RANGE = -10000
MAX_RANGE = 10000
_SORTED_ARRAY = False
# _SORTED_ARRAY = True


def rangedown(s1_index):
    return range(s1_index-1, -1, -1)


def ranged_twosum(my_sorted_data, t_table):
    """
    evaluate if distinct x,t (x != y) values exist
    that make x + y = t (one pair per t), counter += 1 if true
    """
    counter = 0
    len_ = len(my_sorted_data)
    s1_index = len_
    s2_index = 0

    # t_table[0] = LOCAL_MIN
    # t_table[-1] = LOCAL_MAX
    while t_table:
        for i, x in enumerate(my_sorted_data):
            if x*2 >= t_table[-1] or i == len_-1:
                t_table.clear()
                return counter
            if i % 2 == 0:
                # j index goes down
                for j in rangedown(s1_index):
                    if j <= i:
                        s1_index = len_
                        s2_index = j+1
                        break
                    y = my_sorted_data[j]
                    if y*2 <= t_table[0]:
                        t_table.clear()
                        break
                    elif x + y <= t_table[0]:
                        s1_index = len_
                        s2_index = j+1
                        break
                    # else:
                    if t_table[0] <= x + y <= t_table[-1]:
                        try:
                            t_table.remove(x+y)
                            counter += 1
                            if not t_table:
                                return counter
                        except:
                            pass
            else:  # i % 2 != 0:
                # j index goes up
                for j in range(max(s2_index, i+1), s1_index):
                    y = my_sorted_data[j]
                    if x + y >= t_table[-1]:
                        # TODO: there are out of range index concerns
                        s1_index = j-1
                        s2_index = i+1
                        break
                    # else:
                    if t_table[0] <= x + y <= t_table[-1]:
                        try:
                            t_table.remove(x+y)
                            counter += 1
                            if not t_table:
                                return counter
                        except:
                            pass


def main(file_name):
    # take values from file and run topfive_scc_sizes
    with open(file_name) as fh:
        if file_name[:4] == 'test':
            print((fh.readline()).strip())  # remove+show answer from test file

        # remove duplicates via set() datatype
        my_hashed_data = set()
        for line in fh:
            my_hashed_data.add(int(line.strip()))
        my_sorted_data = list(my_hashed_data)
        my_sorted_data.sort()
        print("sorted")

        t_table = [x for x in range(MIN_RANGE, MAX_RANGE+1)]
        xy_pairs = ranged_twosum(my_sorted_data, t_table)

        print("Number of t values matched"
              " by distinct x,y pairs: {}".format(xy_pairs))


if __name__ == '__main__':
    # working with argv to accept file input
    if len(sys.argv) > 2:
        sys.exit("Usage: inv_count <file_name> (leave empty for testing)")
    if len(sys.argv) == 1:
        print("No filename input, testing...")
        unittest.main()
    # else: argv == 2
    main(sys.argv[1])
