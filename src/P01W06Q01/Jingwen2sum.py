'''
Created on 2015

@author: Jingwen Ouyang

Review notes by Ofer:
- assumes data is symmetrically distributed instead of skipping
  buckets based on the bucket x is in.
- time saved by not sorting is insignificant (approximately 0.1 seconds).
- using a set is clearly faster than a method based on a list.
- using buckets of size 10000 is slower than moving j index method
  moving j expectedly makes loops smaller than bucket size.

'''

import time

start = time.time()
input_ = {}

# put input into buckets of 10000
with open('algo1_programming_prob_2sum.txt') as file_in:
    # with open('test5.txt') as file_in:
    for line in file_in:
        x = int(line.strip())
        bucket = x//10000
        if bucket not in input_:
            input_[bucket] = [x]
        else:
            input_[bucket].append(x)
print('input file read finish \t@%.3f' % (time.time()-start))

total = {}
for bucket in input_:  # loop in each bucket
    for x in input_[bucket]:  # loop the elements x in the bucket
        for negBucket in range(-bucket-2, -bucket+1, 1):
            # loop the y bucket which could result in sum in range
            if negBucket in input_:
                for y in input_[negBucket]:  # loop the elements in the y bucket
                    sum = x+y
                    if sum <= 10000 and sum >= -10000 and (not (sum in total)):
                        total[sum] = sum

print('computation finished \t@%.3f' % (time.time()-start))
print('there are total of ***%d*** distinct sum' % len(total))
