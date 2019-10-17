# https://www.hackerrank.com/challenges/between-two-sets/forum
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# 내 풀이
def getTotalX(a, b):
    max_a, max_b, min_b = max(a), max(b), min(b)
    result = []

    for n in range(len(a)):
        if max_a == a[n]:
            continue
        if max_a%a[n] != 0:
            tmp = a[n]
            for k in range(a[n]):
                if a[n]%(k+1) == 0 and max_a%(k+1) == 0:
                    tmp = a[n]/(k+1)
            max_a *= tmp
    
    i = 1
    while i*max_a <= max_b:
        ok = True
        for k in b:
            if k%(i*max_a) != 0:
                ok = False
        if ok:
            result.append(i*max_a)
        i += 1
    print(result)
    return len(result)
    
# 모범답안
# O(n log(n)) solution.
# 1. find the LCM of all the integers of array A. (최소공배수: 집합의 수들이 나눌수 있는 가장 작은 곱셈값)
# 2. find the GCD of all the integers of array B. (최대공약수: 집합의 수들이 나눠지는 가장 큰 나눗셈 값 )
# 3. Count the number of multiples of LCM that evenly divides the GCD.

def gcd(k, l):
    while l>0:
        temp = l
        l = k % l # 이 때 l>k이면 초과된 나머지 값이 나온다 ex) 2%3 => 1
        k = temp
    return k

def arr_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def lcm(k, l): # 문제풀이핵심: 두 수의 최대공약수를 나누면 최소공배수가 된다
    return k*l/gcd(k, l)

def arr_lcm(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result

def getTotalX(arr_a, arr_b):
    a_lcm = arr_lcm(arr_a)
    b_gcd = arr_gcd(arr_b)

    '''
    최소공배수에서 자연수의 곱을 증가시켜가면서 최대공약수값이 나눠지는지 확인한다
    하지만 나누는 값은 최대공약수값보다는 작거나 같아야하므로 while문 조건으로 들어간다.
    '''
    j, count = (1, 0)
    while (a_lcm*j)<=b_gcd: 
        if b_gcd%(a_lcm*j) == 0 : count += 1
        j += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
