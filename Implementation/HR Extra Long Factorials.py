#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/problem

import math
import os
import random
import re
import sys
import functools

def extraLongFactorials(n):
    print(functools.reduce(lambda a, b: a*b, [i for i in range(1, n+1)]))

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
