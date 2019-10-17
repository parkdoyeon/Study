
def print_twod(arr):
    print('-------')
    for row in arr:
        print(row)
    print('-------')

while True:
    col, row = map(int, input().split())
    if col is 0 or row is 0:
        break
    soil = []
    for _ in range(col):
        soil.append(list(input()))
    mark = [[0]*row for _ in range(col)]
    group = 0

    for c in range(col):
        for r in range(row):
            if mark[c][r] is not 0:
                continue

            if soil[c][r] is '*':
                mark[c][r] = -1
            else:
                group += 1
                mark[c][r] = group
                for cadd in range(-1, 2):
                    if c+cadd < 0 or c+cadd >= col: continue
                    for radd in range(-1, 2):
                        if r+radd < 0 or r+radd >= row: continue
                        if soil[c+cadd][r+radd] is '@':
                            if mark[c+cadd][r+radd] is 0:
                                mark[c+cadd][r+radd] = group
                            elif mark[c+cadd][r+radd] < group:
                                mark[c][r] = mark[c+cadd][r+radd]
                                group -= 1
                        else:
                            mark[c+cadd][r+radd] = -1
                        #print_twod(mark)
    # print_twod(mark)
    # print_twod(soil)
    groups = []
    for ls in mark:
        groups.append(max(ls))
    print(max(groups) if max(groups) > 0 else 0)