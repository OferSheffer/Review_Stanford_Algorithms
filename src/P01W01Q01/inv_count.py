'''
Created on Oct 14, 2015
@author: Ofer

Question 1
Download the text file here. (Right click and save link as) 
http://spark-public.s3.amazonaws.com/algo1/programming_prob/IntegerArray.txt

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
 in some order, with no integer repeated. Your task is to compute the number of 
 inversions in the file given, where the ith row of the file indicates the ith 
 entry of an array. Because of the large size of this array, you should 
 implement the fast divide-and-conquer algorithm covered in the video lectures.
'''

'''
Educational Notes:
 Concatenating immutable sequences always results in a new object. This means
 that building up a sequence by repeated concatenation will have a quadratic
 runtime cost in the total sequence length - e.g. like the question about
 repeated merge-sorts on k sequences of length n. To get a linear runtime 
 cost see:  https://docs.python.org/3/library/stdtypes.html
 
Python TimeComplexity: 
 https://wiki.python.org/moin/TimeComplexity

 list - insert is a terrible idea. O(n)
 set item - good idea. O(1)
'''

def Merge_and_CountSplitInv(A,start_index,dimo):
    """
    Merges two similar length presorted sub-slices of A while counting inversions.
    Input: 
    array A, start_index (location of first sub-slice)
    dimo (tuple with (length/2, length/2+length%2)).
    Output: invesrtions (values where i<j, but A[i]>A[j])
    Side Effect: two consecutive A subsections are sorted.
    """
    pass

def Sort_and_Count(A, n, start_index=0):
    """
    Input: array A, length n, start_index(default=0)
    Output: inversions (values where i<j, but A[i]>A[j])
    Side Effect: A is sorted.
    """
    if n=1, return 0    # base case, array of length 1
    else
        # Input: 1st and 2nd halves of current subarray
        dimo=divmod(n,2)
        x=Sort_and_Count(A, dimo[0], start_index)           
        y=Sort_and_Count(A, dimo[0]+dimo[1], start_index+dimo[0])
        # merge the (newly sorted) half-sized subarrays
        z=Merge_and_CountSplitInv(A,start_index,dimo)
    return x+y+z


if __name__ == '__main__':
    pass