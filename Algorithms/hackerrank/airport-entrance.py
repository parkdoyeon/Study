# https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3
times = [7, 10]
n = 6

l, r, mid = min(times)*1, max(times)*(n-1), 0
answer = r
while l <= r:
    mid = (l+r)//2
    passed = []
    tot_passed = 0
    for t in times:
        passed.append(mid//t)
        tot_passed += mid//t
    
    if tot_passed >= n:
        time_passed = [t*p for t, p in zip(times, passed)]
        if max(time_passed) < answer:
            answer = max(time_passed)
        r = mid-1
    else:
        l = mid+1
    print(l, r, mid)

print(answer)