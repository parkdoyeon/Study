
#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# 문제가 제대로 이해 안되어서 시간이 오래걸림. 인덱스 0과 1인 지점에 모두 0이 있으면 1부터 시작해도 되지만,
# 마지막 스텝에 0이 있으면 무조건 밟고 지나가야함! 중요한 조건인데 왜 안적혀있지?
def jumpingOnClouds(c):
    skipnext = False
    idx, jump = 0, 0
    while idx < len(c):
        if c[idx] == 0:
            if idx != 0: jump += 1
            if idx+2 < len(c):
                if c[idx+2] == 0:
                    idx += 1
            idx += 1
        elif c[idx] == 1:
            idx += 1
            continue

    return jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
