braket = str(input())
#l, r = (0, 0)
ar = list(braket)
found = True
cnt, n = (0, 0)
for b in braket:
    if b is '(': n += 1
    else:
        if n is 0:
            cnt += 1
        else:
            n -= 1
print(cnt+n)