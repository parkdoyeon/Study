#!/bin/python3

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
    if not re.search('[!@#$%^&*()\-+]', password):
        point += 1
    if point + n < 6:
        point += 6-(point+n)
    
    return point

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()
    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
