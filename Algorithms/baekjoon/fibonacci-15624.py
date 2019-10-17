#1000000
N = int(input())
a, b, n = (0,1,1)
idx = 2
even_sum = 1
while idx <= N:
    n = (a+b)%1000000007
    a = b
    b = n
    idx += 1
print(n)