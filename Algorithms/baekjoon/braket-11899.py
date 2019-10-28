braket = str(input())
cnt, n = (0, 0)
for b in braket:
    if b is '(': n += 1
    else:
        if n is 0:
            cnt += 1
        else:
            n -= 1
print(cnt+n)