#!/bin/python3

# solved: 2020-01-20
# Hunter Darling

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

	set1 = set(s1)
	set2 = set(s2)
	print(s1)
	print(s2)
	
	if len(set1 & set2) >= 1:
		return "YES"
	else:
		return "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)
		
	print(result)
