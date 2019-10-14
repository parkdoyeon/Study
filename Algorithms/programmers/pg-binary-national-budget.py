budgets = [120, 110, 140, 150]
M =485
right_answer = 127
def my_solution(budgets, M):
    if sum(budgets) <= M: return max(budgets)
    expect = int(M/len(budgets))
    while True:
        ret_sum = 0
        for i in range(len(budgets)):
            if budgets[i] > expect: 
                ret_sum += expect
                continue
            ret_sum += budgets[i]
        
        if ret_sum < M:
            expect += 1
        elif ret_sum > M:
            expect -= 1
            break
        else: break
    return expect

def good_solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    l, r, mid = 1, max(budgets), 0
    answer = 0

    while l <= r:
        mid = (l+r) // 2
        total = 0

        for budget in budgets:
            if budget <= mid:
                total += budget
            else:
                total += mid

        if total > M:
            r = mid - 1
        else:
            if answer <= mid:
                answer = mid
            l = mid + 1
    return answer


l, r, mid = 1, max(budgets), 0
while l <= r:
    mid = l+r//2
    ret_sum = 0
    for i in range(len(budgets)):
        if budgets[i] > mid: 
            ret_sum += mid
            continue
        ret_sum += budgets[i]
    
    if ret_sum <= M:
        if answer <= mid:
            answer = mid
        l = mid+l//2
    elif ret_sum > M:
        r = mid+r//2
    print(l, r, mid)