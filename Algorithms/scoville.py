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

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville) < 2: return -1
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
    
    return answer

일반 .pop()함수도 오래걸렸다

def chk(arr, n):
    for a in arr:
        if a < n: return True
    return False

print(heapsolution([1,2,3,9,10,12], 7))