#https://www.hackerrank.com/challenges/angry-children

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    ret = []
    example = []
    for i in range(len(arr)-k+1):
        k_list = arr[i:i+k]
        example.append(k_list[-1]-k_list[0])
        if chkFair(k_list):
            ret.append(k_list[-1]-k_list[0])
    print(example)
    return min(ret)

def chkFair(karr):
    gap = karr[1]-karr[0]
    for i in range(1, len(karr)-1):
        if karr[i+1]-karr[i] != gap:
            return False
    return True

if __name__ == '__main__':
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result) + '\n')