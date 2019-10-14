braket = str(input())
#l, r = (0, 0)
ar = list(braket)
found = True
while found:
    prev, found = (False, False)
    idx = 0
    for b in ar:
        if b is '(':
            prev = True
        else:
            if prev:
                found = True
                #print('전')
                #print(ar)
                ar.pop(idx)
                ar.pop(idx-1)
                #print(ar)
                #print('끝')
                idx -= 3
                if idx >= 0 and ar[idx] is '(':
                    prev = True
                else:
                    prev = False
            else:
                prev = False
        idx += 1
print(len(ar))
#print(ar)