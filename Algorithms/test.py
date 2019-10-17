import heapq
def solution(estimates, k):
    answer = [sum(estimates[0:k])]
    for idx in range(1, len(estimates)-k):
        print(idx, idx+k+1)
        #heapq.heappush(answer, -(answer[idx-1]-estimates[idx-1]+estimates[idx+k+1]))
        answer.append(answer[idx-1]-estimates[idx-1]+estimates[idx+k+1])
    #return heapq.heappop(answer)*(-1)
    return max(answer)

solution([1, 1, 9, 3, 7, 6, 5, 10], 4)