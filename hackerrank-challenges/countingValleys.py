#!/bin/python3

#solved 2020-01-19
#Hunter Darling

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    v = 0 
    d = 0
    l = list(s)
    for i in l:
        if i == 'U':
            d += 1
        else:
            d -= 1
        if i == 'U' and d == 0:
            v += 1

    return v


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    
    print(result)

