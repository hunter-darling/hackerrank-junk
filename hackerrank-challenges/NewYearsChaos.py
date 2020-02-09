#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    result = 0
    #i = 0
    #t = list(range(len(q)+1))
    #t.remove(0)
    #print(q)
    #print(t)
    for i in range(len(q)-1,-1,-1):
        if (q[i] - (i + 1)) > 2:
            print('Too chaotic')
            return
        for h in range(max(0, q[i] - 2),i):
            if q[h] > q[i]:
                result+=1
    print(result) 
    


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
