# https://www.hackerrank.com/challenges/ctci-making-anagrams/
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
# 내 풀이: 집합개념을 통해 딕셔너리로 갯수계산 1차로 끝내고, 만들어진 딕셔너리 자료형의 갯수를 두번때 단어를 순회하면서 삭제해주었다
# 집합 변환하고 계산하는 비용이 좀 있어서 약간 복잡한느낌
def makeAnagram(a, b):
    aset = set(list(a))
    bset = set(list(b))
    a_diff = aset.difference(bset)
    b_diff = bset.difference(aset)
    ab_shared = aset.intersection(bset)
    ab_shared_count = dict.fromkeys(ab_shared, 0)
    ret = 0
    for s in a:
        if s in a_diff: ret += 1
        elif s in ab_shared: ab_shared_count[s] += 1
    for s in b:
        if s in b_diff: ret += 1
        elif s in ab_shared: ab_shared_count[s] -= 1

    for count in ab_shared_count.values():
        ret += abs(count)
    
    return ret


# discussion 풀이: 문자열을 숫자값을 가진 인덱스로 변환하고, 해당 인덱스에 있는 갯수를 두번째 단어를 순회하면서 차감하고
# 최종적으로 차감되지 못한 단어가 있는지를 직접 센다
from math import fabs

def number_needed(a, b):
    letterArray = [0] * 26
    for c in a:
        index = ord(c) - ord('a')
        letterArray[index]+=1
    for c in b:
        index = ord(c) - ord('a')
        letterArray[index]-=1
    result = 0
    for i in letterArray:
        result += fabs(i)
    return int(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
