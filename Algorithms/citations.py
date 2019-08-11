def solution_tmp(citations):
    
    citations.sort()
    l, r = citations[0], citations[-1:][0]
    mid = (l+r)//2
    answer = mid
    while l < r:
        mid = (l+r)//2
        if len(citations) < mid+1:
            r = mid-1
            continue
            
        les, mor = 0, 0
        for c in citations:
            if c < mid:
                les += 1
            elif c > mid:
                mor += 1
            else:
                les += 1
                mor += 1
        print(l, r, mid)
        if mor >= mid and les <= mid:
            answer = mid
            break
        elif mor < mid:
            r = mid-1
        elif mor > les:
            l = mid+1
    return answer

def solution(citations):
    citations.sort()
    mid = len(citations)//2
    print(mid, citations[mid:])
    hidx = citations[mid]
    while True:
        if hidx < citations[mid]:
            mid += 1
        elif hidx > citations[mid]:
            if hidx <= citations[mid+1] and len(citations[mid+1]) >= citations[mid+1]:
                answer = citations[mid+1]
                return answer
            mid -= 1
        else: return hidx

print(solution([3, 0, 6, 1, 5]))