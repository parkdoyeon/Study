# https://www.hackerrank.com/challenges/strong-password/problem

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    point = 0
    if not re.search('[0-9]', password):
        point += 1
    if not re.search('[a-z]', password):
        point += 1
    if not re.search('[A-Z]', password):
        point += 1
    if not re.search('[!@#$%^&*()\-+]', password): #'-' escpae 빼먹지 말것
        point += 1
    if point + n < 6:
        point += 6-(point+n)
    
    return point

# 조금 더 깔끔한 로직
# def minimumNumber(n, password):
#     count = 0
#     cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'[!@#$%^&*()\-+]']
#     for case in cases:
#         if not re.search(case, password):
#             count += 1

#     return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()
    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
