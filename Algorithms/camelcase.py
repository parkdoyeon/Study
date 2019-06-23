# https://www.hackerrank.com/challenges/camelcase/problem

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    wordscount = 1
    for char in s:
        if ord(char) <= ord('Z'): wordscount += 1
    return wordscount

# O(1) in java 
# System.out.println(s.length() - s.replaceAll("[A-Z]", "").length() + 1);

if __name__ == '__main__':
    s = input()

    result = camelcase(s)

    print(str(result) + '\n')
