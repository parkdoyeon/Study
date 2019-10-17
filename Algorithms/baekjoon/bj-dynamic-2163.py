bars = [[-1]*300]*300

def split(n, m):
    if n is 1:
        return m-1

    if bars[n][m] is -1:
        return split(n-1, m)+split(1, m)+1
    else:
        return bars[n][m]

nums = input().split()
input_list = list(map(int, nums))
ans = split(input_list[0], input_list[1])
print(ans)