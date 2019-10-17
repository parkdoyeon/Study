
# https://www.hackerrank.com/challenges/encryption/problem
# 내 풀이

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.strip()
    num = math.sqrt(len(s))
    row = int(num)
    array = []
    counts = row if row**2 == len(s) else row+1
    for i in range(counts):
        array.append(s[i::counts])
    return ' '.join(array)


# 모범 답안

import sys
from math import ceil, sqrt

s=input().strip()
exec("print(' '.join(map(lambda x: s[x::{0}], range({0}))))".format(ceil(sqrt(len(s)))))


# 실행

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
