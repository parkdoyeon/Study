#https://www.hackerrank.com/challenges/the-birthday-bar/problem
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    if m > d: return count

    if m == 1:
        for i in s:
            if i == d: count += 1
    else:
        # [1, 2, 3][:0]은 []을 리턴한다! 주의할것.
        for i in range(len(s[:-m+1])):
            if sum(s[i:i+m]) == d: count += 1

    return count

# 위의 로직에서 변형
def birthday(s, d, m):
    count = 0
    if m > d: return 0

    for i in range(len(s)):
        if len(s[i:i+m]) != m: break # [1, 2, 3][:0]은 []을 리턴한다! 주의할것.
        if sum(s[i:i+m]) == d: count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])

    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()
