#!/bin/python3
# https://www.hackerrank.com/challenges/larrys-array/problem

'''
To sort the array, the number of inversions must be reduced to zero.
An inversion is a swap between any two items matching: (a,b) -> (b,a) when a > b.
If the number of required inversions is odd, 
we can never reduce all inversions to zero using rotations, 
since rotations always affect an even number of inversions.

Examples:

Suppose we have the array [3,1,2]:

Total number of inversions:
(3,1) is an inversion (3 > 1).
(3,2) is an inversion (3 > 2).
(1,2) is not an inversion.
Total inversions: 2 (even).

Since the number of inversions is even, the code would return "YES", indicating that the array can be sorted with 3-element rotations.

For the array [3,2,1]:

Total number of inversions:
(3,2) is an inversion.
(3,1) is an inversion.
(2,1) is an inversion.
Total inversions: 3 (odd).

Since the number of inversions is odd, the code would return "NO", indicating that it is not possible to sort this array with only 3-element rotations.
'''

import math
import os
import random
import re
import sys

def larrysArray(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                count += 1
                
    if count % 2 == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
