# https://programmers.co.kr/learn/courses/30/lessons/43237?language=python3
budgets = [120, 110, 140, 150]
M = 485
if sum(budgets) <= M: print(max(budgets))
else:
    expect = int(M/len(budgets))
    while True:
        ret_budgets = budgets[:]
        for i in range(len(ret_budgets)):
            print(ret_budgets)
            if ret_budgets[i] <= expect: continue
            else:
                print(str(expect)+' 할당')
                ret_budgets[i] = expect
        if sum(ret_budgets) < M:
            expect += 1
            print(expect)
        elif sum(ret_budgets) > M:
            expect -= 1
            break
        else: break
    print(expect)