# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    right = 0
    left = 0
    for n in range(len(arr)):
        right += arr[n][len(arr)-1-n]
        left += arr[n][n]
    if right*left < 0: #부호가 다른 절대값의 연산은 뺄셈 순서를 바꿔줘야한다
        return abs(right-left) if right > left else abs(left-right)
    return abs(right-left)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')