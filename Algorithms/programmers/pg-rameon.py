# import collection
# def solution(stock, dates, supplies, k):
#     answer = 0
#     while stock < k:
#         idx = 0
#         # 공급가능일 찾기
#         for i in range(len(dates)):
#             if stock >= dates[i]:
#                 idx = i
#             else: 
#                 break
#         # 최대 일 찾기
#         maxsup = max(supplies[:i+1])
#         popidx = supplies[:i+1].index(maxsup)
#         # 찾으면 공급일 제외하고 stock에 더하기
#         stock += maxsup
#         answer += 1
#         dates.pop(popidx)
#         supplies.pop(popidx)
#     return answer

import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    date_sup = list(zip(supplies, dates))
    print(supidx)
    while stock-1 < k:
        idx = 0
        for d, s in date_sup:
            if stock >= d:
                
        # 공급가능일 찾기
        for i in range(len(dates)):
            if stock >= dates[i]: idx = i
            else: break
        
        # 최대 공급 찾기
        tmp = supplies[0]
        for s, i in supplies, range(len(supplies)):
            if i < idx:
                if tmp < s:
                    tmp = s
        suptmp = supidx[:i+1]
        print(suptmp)
        maxitem = heapq.nlargest(0, suptmp, key=lambda x: x[0])
        print(maxitem)
        # 찾으면 공급일 제외하고 stock에 더하기
        stock += maxitem[0]
        answer += 1
        dates.pop(maxitem[1])
        supidx.pop(maxitem[1])
    return answer

solution(4, [4,10,15],[20,5,10],30)
