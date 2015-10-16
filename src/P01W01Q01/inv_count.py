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

def Sort_and_Count(A, n, start_index=0):
    """
    Input: array A, length n, start_index(default=0)
    Output: inversions (values where i<j, but A[i]>A[j])
    Side Effect: A is sorted.
    """
    if n=1, return 0    # base case, array of length 1
    else
        x=Sort_and_Count(A, n/2, start_index)           # Input 1st half of A
        y=Sort_and_Count(A, n/2+n%2, start_index+n/2)   # Input 2nd half of A
        
        z=Merge_and_CountSplitInv(B,C,n)    # sorted 1st and 2nd halves
        
    return x+y+z


if __name__ == '__main__':
    pass