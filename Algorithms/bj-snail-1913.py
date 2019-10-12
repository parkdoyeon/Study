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
while num is not flag:
    # up
    col = col+up
    num += 1
    dr[col][row] = num
    up = up+1 if up > 0 else up-1
    print_two_d(dr)

    # right
    row = row+right
    num += 1
    dr[col][row] = num
    right = right+1 if right > 0 else right-1
    print_two_d(dr)

    # bottom
    for i in range(bottom):
        col = col+1
        num += 1
        dr[col][row] = num
        bottom = bottom+1 if bottom > 0 else bottom-1
        print_two_d(dr)

    # left
    row = row+left
    num += 1
    dr[col][row] = num
    left = left+1 if left > 0 else left-1
    print_two_d(dr)

print_two_d(dr)