# zcnt = 0
# ocnt = 0
# def fibo(n):
#     if n is 0:
#         global zcnt 
#         zcnt += 1
#         return 0
#     if n is 1:
#         global ocnt
#         ocnt += 1
#         return 1
#     return fibo(n-1)+fibo(n-2)
# 위의 방식은 시간초과 일어남.

def getcnt(n):
    if n is 0:
        return [1, 0]
    if n is 1:
        return [0, 1]
    zcnt, ocnt = getcnt(n-1)
    return [ocnt, zcnt+ocnt]

case = int(input())
for _ in range(case):
    num = int(input())
    zcnt, ocnt = getcnt(num)
    print(str(zcnt)+' '+str(ocnt))