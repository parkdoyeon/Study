#1000000000000000000
N = int(input())
# one, two, three = (0,1,1)
# idx = 3
# even_sum = 1
# while idx <= N+1:
#     temp = three
#     three = two+three
#     one = two
#     two = temp
#     idx += 1
# print(three-1)

def fibo(n):
    if n is 0: return 0
    if n is 1: return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(N+1)-1)