from collections import defaultdict
def solution(stock, dates, supplies, k):
    answer = 0
    while stock < k-1:
        #흐름이 끊기지 않는 경우의 수
        option_day_idx = 0
        for i in range(len(dates)):
            if dates[i] > stock:
                option_day_idx = i
                break
        
        #최소한의 공급을 받는 경우
        print(option_day_idx)
        option_sup = sorted(supplies[:option_day_idx])
        pop_sup = option_sup.pop()
        sup_idx = supplies.index(pop_sup)
        stock += pop_sup
        dates.pop(sup_idx)
        supplies.pop(sup_idx)
        answer += 1
    
    return answer

print(solution(4,[4,10,15],[20,5,10],30))