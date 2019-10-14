#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    unsorted.sort(key=int)
    return unsorted

# 내가 개발한 bigsort, 제출시 절반만 통과하고 타임아웃이 발생했다.
# def bigSorting(unsorted):
#     for i in range(len(unsorted)-1, -1, -1):
#         lgidx, largest = i, unsorted[i]
#         j = -1
#         while i+j >= 0:
#             if len(unsorted[j+i]) > len(largest):
#                 lgidx = j+i
#                 largest = unsorted[j+i]
#             elif len(unsorted[j+i]) == len(largest):
#                 if int(unsorted[j+i]) > int(largest):
#                     lgidx = j+i
#                     largest = unsorted[j+i]
#             j-=1
#         if unsorted[i] != largest:
#             temp = unsorted[i]
#             unsorted[i] = largest
#             unsorted[lgidx] = temp
#     return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
