#!/bin/python3

import math
import os
import random
import re
import sys

# This is not having "valleys" in count, so declined
'''
def surfaceAreaDeclined(A):
    # Write your code here
    print(A)
    
    front = []
    areaFront = 0
    for i in range(0, len(A)):
        maxFront = 0
        for j in range(0, len(A[i])):
            if A[i][j] > maxFront:
                maxFront = A[i][j]
        areaFront += maxFront
    print(f"areaFront: {areaFront}")

    print(A)
    areaSide = 0
    for j in range(0, len(A[0])):
        maxSide = 0
        for i in range(0, len(A)):
            #print(A[i][j])
            if A[i][j] > maxSide:
                maxSide = A[i][j]
        areaSide += maxSide
    print(f"areaSide: {areaSide}")
    
    areaTop = 0
    for i in range(0, len(A)):
        areaTop = areaTop + len(A[i])
    print(f"areaTop: {areaTop}")
    
    total = 2*areaFront + 2*areaSide + 2*areaTop
    return total
'''
    
def hasNeighbour(A, i, j, k):
    if i < 0 or j < 0 or k < 0:
        return False
    try:
        A[i][j][k]
        return True
    except IndexError:
        return False
    
def getNeighbours(A,i,j,k):
    neighbours = 0
    
    if hasNeighbour(A, i-1, j, k):
        neighbours += 1
    if hasNeighbour(A, i+1, j, k):
        neighbours += 1
    if hasNeighbour(A, i, j+1, k):
        neighbours += 1
    if hasNeighbour(A, i, j-1, k):
        neighbours += 1
    if hasNeighbour(A, i, j, k+1):
        neighbours += 1
    if hasNeighbour(A, i, j, k-1):
        neighbours += 1
    return neighbours

def surfaceArea(A):
    totalArea = 0
    B = [[[1 for k in range(0, A[i][j])] for j in range(0, len(A[i]))] for i in range(0, len(A))]
    print(B)
    surface = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            for k in range(len(B[i][j])):
                neighbours = getNeighbours(B,i,j,k)
                surface = surface + (6-neighbours)
    return surface
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
