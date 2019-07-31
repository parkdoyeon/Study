from collections import deque

def solution(scoville, K):
    sco = deque(sorted(scoville))
    answer = 0
    while chk(sco, K):
        if len(sco) < 3: return -1
        answer += 1
        sco.appendleft(sco.popleft()+(sco.popleft()*2))
        print(sco)
    
    return answer

import heapq

def heapsolution(scoville, K):
    sco = scoville
    print(sco)
    answer = 0
    while sco[0] < K:
        if len(sco) < 3: return -1
        answer += 1
        heapq.heappush(sco, heapq.heappop(sco)+(heapq.heappop(sco)*2))
        print(sco)
    
    return answer


def chk(arr, n):
    for a in arr:
        if a < n: return True
    return False

print(heapsolution([1,2,3,9,10,12], 7))