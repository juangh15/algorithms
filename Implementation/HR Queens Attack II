#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem

import math
import os
import random
import re
import sys

def putInChessBoard(r, c, n):
    i = n - r
    j = c - 1
    return i,j
    
def printBoard(B):
    a = ""
    for r in B:
        for c in r:
            a = a + str(c) + "  "
        a += "\n"
    print(a)
    
def getDirection(qi, qj, i, j, n):
    # Horizontal
    if qi == i:
        # Horizontal distance - 1 meaning the step of obstacle is not reachable
        if qj - j > 0:
            return abs(qj-j)-1, 'left'
        else:
            return abs(qj-j)-1, 'right'
    
    # Vertical
    if qj == j:
        # Vertical distance - 1 meaning the step of obstacle is not reachable
        if qi - i > 0:
            return abs(qi-i)-1, 'up'
        else:
            return abs(qi-i)-1, 'down'
    
    # Diagonal
    if abs(qi - i) == abs(qj - j):
        # Diagonal distance - 1 meaning the step of obstacle is not reachable
        bound = max(abs(qi-i), abs(qj-j)) - 1
        if (qi - i) > 0 and (qj - j) > 0:
            return bound,'up-left'
        if (qi - i) < 0 and (qj - j) < 0:
            return bound,'down-right'
        if (qi - i) > 0 and (qj - j) < 0:
            return bound,'up-right'
        if (qi - i) < 0 and (qj - j) > 0:
            return bound,'down-left'
            
        # It is the same point
        return 0,None

    # It is NOT an obstacle
    return None,None

def queensAttack(n, k, r_q, c_q, obstacles):
    
    # Obtain indexes i,j for queen
    qi, qj = putInChessBoard(r_q, c_q, n)
    
    # Dictionary with bounds for all directions in which the queen can move
    bounds = {}
    
    # Cross directions 
    bounds['up']    = qi
    bounds['left']  = qj
    bounds['right'] = n - 1 - qj
    bounds['down']  = n - 1 - qi
    
    # Diagonal directions
    bounds['up-left']       = min(bounds['up']  , bounds['left'])
    bounds['up-right']      = min(bounds['up']  , bounds['right'])
    bounds['down-right']    = min(bounds['down'], bounds['right'])
    bounds['down-left']     = min(bounds['down'], bounds['left'])
    
    for o in obstacles:
        i,j = putInChessBoard(o[0], o[1], n)
        bound, direction = getDirection(qi, qj, i, j, n)
        
        if direction:
            #print(f"{i} {j}")
            #print(direction)
            #print(bound)
            if bound < bounds[direction]:
                bounds[direction] = bound
    total = 0
    for k in bounds.keys():
        total = total + bounds[k]
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
