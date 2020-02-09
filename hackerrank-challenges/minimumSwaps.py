#!/bin/python3

#solved 2020-01-19
#Hunter Darling

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    
    swaps = 0
    i = 0
    while i < (len(arr)-1):
        if arr[i] == i+1:
            i+= 1
        else:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            swaps += 1
            
    return swaps


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    
    print(res)
