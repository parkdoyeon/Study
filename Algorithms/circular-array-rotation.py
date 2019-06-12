#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries): 
    '''
    slicing은 범위에 대한 표현이기때문에 인덱스 범위 체크를 하지 않는다.
    k가 전체 길이보다 커져버리면 a[-k:]는 전체배열을 리턴하기 때문에, 원점으로 돌아오는 시점을 제외하고 카운트하는게 적절하다.
    '''
    k = k%n if k >len(a) else k 
    
    a = a[-k:]+a[:-k]
    return [a[q] for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
