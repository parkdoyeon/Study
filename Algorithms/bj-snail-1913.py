def print_two_d(arr):
    for row in arr:
        print(row)

N = 7
dr = [[-1]*N for i in range(N)]
middle = N//2
col, row = (middle, middle)
up, right, bottom, left = (-1, 1, 2, -2)
num = 1
flag = N*N
dr[middle][middle] = num
dr[0][0] = flag
print_two_d(dr)
while num < flag:
    # up
    for i in range(abs(up)):
        col += 1 if up > 0 else -1
        num += 1
        if num >= flag: break
        dr[col][row] = num
        print_two_d(dr)
    up = up+2 if up > 0 else up-2
    #print_two_d(dr)
    if num >= flag :break
    # right
    for i in range(abs(right)):
        row += 1 if right > 0 else -1
        num += 1
        dr[col][row] = num
    right = right+2 if right > 0 else right-2

    # bottom
    for i in range(abs(bottom)):
        col += 1 if bottom > 0 else -1
        num += 1
        dr[col][row] = num
    bottom = bottom+2 if bottom > 0 else bottom-2
    #print_two_d(dr)

    # left
    for i in range(abs(left)):
        row += 1 if left > 0 else -1
        num += 1
        dr[col][row] = num
    left = left+2 if left > 0 else left-2
    #print_two_d(dr)

print_two_d(dr)