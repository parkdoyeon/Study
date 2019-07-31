
def solution(progresses, speeds):
    deploy = [0]*len(progresses)
    day = 0
    while 0 in deploy:
        day += 1
        for i in range(len(progresses)):
            if deploy[i] is 0 and progresses[i]+speeds[i]*day >= 100:
                deploy[i] = day
    
    predeploy = deploy[0]
    for i in range(1, len(deploy)):
        if predeploy >= deploy[i]:
            deploy[i] = predeploy
        predeploy = deploy[i]
    
    print(deploy)
    tmp = sorted(list(set(deploy)))
    answer = []
    for t in tmp:
        answer.append(deploy.count(t))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))