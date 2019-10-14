#https://www.hackerrank.com/challenges/luck-balance
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp, unimp = [], []
    for i in contests:
        if i[1]:
            imp.append(i[0])
        else:
            unimp.append(i[0])
    
    imp.sort()
    savedluck = 0
    for i in range(k):
        if len(imp) == 0: break
        savedluck += imp.pop()
    for i in unimp:
        savedluck += i 
    
    return savedluck-sum(imp)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()


# O(N), 소팅을 역으로 한 다음에 종류에 따라 순차적으로 깎는다. 한번만 순회.
def luckBalance(k, contests):
    # sort from greatest luck to least luck
    contests.sort(reverse=True) # 소팅 할때 파이썬은 2차원의 경우 제일 앞의 원소를 기준으로 소팅한다는 점 기억할것
    luck = 0

    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif k > 0:
            luck += contest[0]
            k -= 1
        else: # 지는 케이스 찾기가 완료되면 운에서 깎기
            luck -= contest[0]

    return luck