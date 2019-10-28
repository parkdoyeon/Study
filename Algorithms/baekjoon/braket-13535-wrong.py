N = int(input())
braket = str(input())
cnt, n, other = (0, 0, 0)
for b in braket:
    if b is '(': n += 1
    else:
        if n > 0:
            cnt += 1
            n -= 1
        else:
            other += 1
if other is 0: print(cnt)
else: print(0)