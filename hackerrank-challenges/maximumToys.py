#!/bin/python3

# solveed: 2020-01-20
# Hunter Darling

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):

    lst = []
    s = 0
    p = prices.sort()
    for i in prices:
        if s + i < k:
            lst.append(i)
            s+=i
    return len(lst)


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    print(result)
