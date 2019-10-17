#1000000000000000000
N = int(input())
a,b,n = (0,1,1)
idx = 3
even_sum = 1
while idx <= N:
    n = a+b
    a = b
    b = n
    idx += 1
# def fibo(n):
#     if n is 0: return 0
#     if n is 1: return 1
#     return fibo(n-1)+fibo(n-2)

print(n)