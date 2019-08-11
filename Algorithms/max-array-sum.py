#!/bin/python3

import math
import os
import random
import re
import sys

ary = []

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    odd = arr[0::2]
    even = arr[1::2]
    print(odd, even)
    k = 2
    while k < len(arr)-1:
        j = 0
        while j < len(arr)-2: 
            last = 0
            for i in range(j, len(arr), k):
                ary.append(last + arr[i])
                last = last + arr[i]
            j += 1
        k += 1
    return max(ary)

def findSubArr(arr, count):

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
