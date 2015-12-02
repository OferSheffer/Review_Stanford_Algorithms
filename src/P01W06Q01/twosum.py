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
Run index i up on data. Index j starts at the end and goes down and up like
a pendulum while the joint values x+y fit the MAX/MIN values left in t-table.
If a t value is noticed it is popped out to avoid duplication in the counts.
Main advantage of this method – we don’t review many values that have no
chance of being in the range.

'''

import sys
import unittest
# from multiprocessing import Pool

MIN_RANGE = -10000
MAX_RANGE = 10000


def rangedown(length):
    """range: from top-1 to 0"""
    return range(length-1, -1, -1)


def ranged_twosum(my_sorted_data, t_table):
    """
    evaluate if distinct x,t (x != y) values exist
    that make x + y = t (one pair per t), counter += 1 if true
    """
    counter = 0
    len_ = len(my_sorted_data)
    bottom_idx = 0
    top_idx = len_

    # t_table[0] - local minimum , t_table[-1] = local maximum
    while t_table:
        for i, x in enumerate(my_sorted_data):
            if x*2 >= t_table[-1] or i == len_-1:  # too big
                t_table.clear()
                return counter

            # j index going down
            if i % 2 == 0:
                for j in rangedown(top_idx):
                    if j <= i:
                        bottom_idx = j+2  # TODO: index concerns
                        break
                    y = my_sorted_data[j]
                    if x + y < t_table[0]:  # too small
                        bottom_idx = j+1
                        break
                    elif t_table[0] <= x + y <= t_table[-1]:  # in range
                            try:
                                t_table.remove(x+y)  # Note: slow idea
                                counter += 1
                                if not t_table:
                                    return counter
                            except:
                                pass
                    else:  # x + y > t_table[-1]
                        continue

            # j index going up
            else:  # i % 2 != 0:
                # j index goes up
                for j in range(max(bottom_idx, i+1), top_idx):
                    y = my_sorted_data[j]
                    if x + y > t_table[-1]:  # too big
                        xplus = my_sorted_data[i+1]
                        while(j <= len_ and xplus + y <= t_table[-1]):
                            y = my_sorted_data[j]
                            j += 1
                        top_idx = j-1
                        bottom_idx = max(bottom_idx, i+2)  # TODO: index concerns
                        break
                    elif t_table[0] <= x + y <= t_table[-1]:  # in range
                        try:
                            t_table.remove(x+y)  # Note: slow idea
                            counter += 1
                            if not t_table:
                                return counter
                        except:
                            pass
                    else:  # x + y < t_table[0]
                        continue


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
