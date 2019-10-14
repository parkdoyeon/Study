# https://www.hackerrank.com/challenges/two-characters/problem

import math
import os
import random
import re
import sys

# Complete the alternate function below.
# 내답안 O(n*logn)
def alternate(s): 
    tup = tuple(set(s))
    count = 0

    for i in range(len(tup)-1):
        one = tup[i]
        j = 1
        while(j+i <= len(tup)-1):
            two = tup[j+i]
            ok, tmp = chkvalidity(one, two, s)
            if ok and tmp > count: count = tmp
            j += 1
    return count 


# def chkvalidity(one, two, lis):
#     chars = set(lis) - set(one) - set(two) # 사용할 단어 제외
#     tup = tuple(chars)
#     for i in tup: lis = lis.replace(i, '') # 사용할 단어만 남기고 제거
    
#     pre = ''
#     ok, count = (True, len(lis))
#     for i in lis: # 이전 값이랑 중복 있는지 체크
#         if pre == '':
#             pre = i
#             continue
#         if pre == i:
#             ok = False
#             break
#         pre = i
#     return ok, count

# 정규식을 통해 반복찾기
def chkvalidity(one, two, lis):
    chars = set(lis) - set(one) - set(two) # 사용할 단어 제외
    tup = tuple(chars)
    for i in tup: lis = lis.replace(i, '') # 사용할 단어만 남기고 제거
    ok, count = ( re.search('\S*(.)\1\S*', lis), len(lis))
    return ok, count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
