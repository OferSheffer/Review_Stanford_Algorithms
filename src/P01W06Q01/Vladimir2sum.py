'''
Created on 2015

@author: Vladimir Lyutin

Review notes by Ofer:
- intv maintains max+mix assuming all in between values are desirable.
- using arrt makes it faster to save t values with low memory cost
- I reworked `arr[i] > 0` to `arr[i]*2 > intv[1]`:
  original fails in case data is not evenly distributed.


'''

arr = set()

file = open('algo1_programming_prob_2sum.txt', 'r')
for line in file:
    arr.add(int(line.rstrip()))
file.close()

arr = list(arr)
arr.sort()

intv = [-10000, 10000]
arrt = set()

j = len(arr) - 1
for i in range(0, len(arr)):
    if arr[i]*2 > intv[1] or j < 0:
        break
    while (j < len(arr) - 1) and (intv[1] >= arr[i] + arr[j]):
        j += 1
    while intv[0] <= arr[i] + arr[j]:
        if intv[1] >= arr[i] + arr[j]:
            arrt.add(arr[i] + arr[j])
        j -= 1

print(len(arrt))
