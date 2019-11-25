
def compressWord(word, K):
    # Write your code here
    ans = word
    found = True
    while found:
        found, ans = removeNtimes(ans, K)
    return ''.join(ans)

def removeNtimes(arr, N):
    # found = False
    # cnt = len(arr)
    # for i in range(len(arr)-K+1):
    #     if i != cnt-1 and arr[i] != arr[i+1]:
    #         continue
    #     if arr[i]*K == arr[i:i+K]:
    #         found = True
    #         return found, arr[:i]+arr[i+K:]
    # return found, arr
    buff, cnt = None, 1
    found = False
    ret = []
    for i in range(len(arr)):
        if buff is None:
            ret.append(arr[i])
            buff = arr[i]
        else:
            ret.append(arr[i])
            if buff == arr[i]:
                cnt += 1
                if cnt == N:
                    for _ in range(N):
                        ret.pop()
                    found = True
            else:
                buff = arr[i]
                cnt = 1
    return found, ret

print(compressWord('abbcccb', 3))