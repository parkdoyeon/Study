def solution(brown, red):
    answer = []
    rw, rh = 1, 1
    while len(answer) == 0:
        tmprh = rh
        while rw >= tmprh:
            print(rw, tmprh)
            if rw*tmprh == red and rw*2+tmprh*2+4 == brown:
                answer = [rw+2, tmprh+2]
                break
            elif rw*2+tmprh*2+4 < brown:
                tmprh += 1
            else:
                break
        rw += 1
        if rw*2+rh*2+4 > brown:
            break
    return answer

print(solution(24, 24))

# item**(0.5) == 루트계산
def good_solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]


# 이렇게하면 빨간 카펫이 정수로 나눠떨어지지 않는 부분 확인이 되지 않는다.
# 테스트케이스 3개 통과 못함.
import math
def wrong_solution(brown, red):
    square = brown+red
    #w = 3 if int(math.sqrt(red)) < 3 else int(math.sqrt(red))+1
    #h = 3 if int(math.sqrt(red)) < 3 else int(math.sqrt(red))+1
    w, h = 3, 3
    answer = []
    while len(answer) == 0:
        tmph = h
        while w >= tmph:
            if w*tmph < square:
                tmph += 1
            elif w*tmph == square:
                answer = [w, tmph]
                break
            elif w*tmph > square:
                break
        w += 1
        if w*h > square:
            break
    
    return answer