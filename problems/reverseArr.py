#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    for i in range(len(a)//2):
        t = a[i]
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = t
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
