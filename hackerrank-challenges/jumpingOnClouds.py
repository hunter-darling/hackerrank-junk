#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    a = -1
    i = 0

    while i < n:
        if i < n-2 and c[i+2] == 0: i += 1
        a += 1
        i += 1

    return a

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    
    print(result)
