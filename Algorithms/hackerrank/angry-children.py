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
    for i in range(len(arr)-k+1):
        #k_list = arr[i:i+k]  이렇게 했더니 복사하는 과정에서 인덱싱이 일어나는게 부하를 주는지 타임아웃 3건이 발생했다.
        #ret.append(k_list[-1]-k_list[0])

        # 직접 접근으로 연산 했더니 성공함 
        ret.append(arr[i+k-1]-arr[i])
    return min(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
