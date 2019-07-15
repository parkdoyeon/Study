
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
# 딕셔너리/집합이 더 리스트보다 검색속도가 빠르다 정해진 내장규척을 통해 해싱이 되어있기때문에 집합을 iterable하게 바꿔도 순서가 바뀌진 않는다.
def pairs(k, arr):
    arr = set(arr)
    ret = 0
    for i in arr:
        if i-k in arr: ret += 1
    return ret

# 딕셔너리 
def pairs(a, k)
    d = {}
    answer = 0
    for i in a:
        d[i] = i
    for j in a:
        g = j+k
        if g in d:
            answer +=1
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
