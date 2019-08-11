from collections import defaultdict

def solution(clothes):
    items = defaultdict(lambda:list())
    for i, k in clothes:
        items[k].append(i)
        
    answer = 1
    for key in items.keys():
        answer *= len(items[key])+1
    return answer-1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))