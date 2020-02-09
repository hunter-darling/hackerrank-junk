#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    dict={}

    count=0

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):

            l1= list(s[i:j].strip())

            l1.sort()

            transf = ''.join(l1)
        
            if transf in dict: 

                count+=dict[transf]

                dict[transf]=dict[transf]+1

            else: 
                
                dict[transf]=1  
            
            print(l1) 
            print(transf)
            print(dict)   

    return count

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

    print("anagrams: ", result)
