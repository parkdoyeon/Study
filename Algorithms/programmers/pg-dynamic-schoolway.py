dp = []
def solution(m, n, puddles):

    for i in range(n):
        way = []
        for j in range(m):
            if i is 0 or j is 0:
                way.append(1)
                continue
            
            if [j+1, i+1] in puddles:
                way.append(0)
                continue
            way.append(dp[i-1][j]+way[j-1])
        dp.append(way)
    answer = dp[n-1][m-1]
    return answer%1000000007

print(solution(1,9,[[2,2]]))
print(dp)