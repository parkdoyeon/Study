def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    right = [check(one, answers), check(two, answers), check(three, answers)]
    tot = max(right)
    return [idx+1 for idx in range(3) if right[idx] == tot]

def check(arr, ans):
    right = 0
    for i in range(len(ans)):
        if ans[i] == arr[i%len(arr)]:
            right += 1
    return right

# ==는 값비교, is는 레퍼런스비교. 
# None, True, False 비교할때만 is 사용하는것이 안전함