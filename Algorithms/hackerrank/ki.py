def solution(stock, dates, supplies, k):
    day = stock
    answer = 0
    daysup = [(d,s) for d, s in zip(dates,supplies)]
    while day < k-1:
        idx = 0
        for i in range(len(daysup)):
            if day < daysup[i][0]:
                idx = i
                break
        print(idx)
        tmp = sorted(daysup[:idx], key=lambda x: x[1])
        day += tmp.pop()[1]
        answer += 1

solution(4, [4,10,15], [20,5,10], 30)