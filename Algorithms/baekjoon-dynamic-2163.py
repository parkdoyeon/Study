
bars = [[-1]*300]*300

def split(n, m):
    if n is 1:
        return m-1

    if bars[n][m] is -1:
        return split(n-1, m)+split(1, m)
    else:
        return bars[n][m]

if __name__ == '__main__':
    n = int(input())
    input_list = []

    for _ in range(n):
        input_list.append(list(map(int, input().rstrip().split())))

    print(split(input_list[0], input_list[1]))
