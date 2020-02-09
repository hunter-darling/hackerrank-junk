#!/bin/python3

#solved 2020-01-19
#Hunter Darling

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    l = len(s)
    #print(l)
    c_temp = s.count('a')
    #print(c_temp)
    q = int(math.floor(n/l))
    #print(q)
    r = n%l
    #print(r)
    if r == 0:
        c = q*c_temp
    else: 
        c = q*c_temp + s[:(r)].count('a')

    return(c)

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    
    print(result)
