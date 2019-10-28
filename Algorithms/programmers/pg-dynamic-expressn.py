dp = [0, 2,]+[-1]*32001
def solution(N, number):
    i = 0
    while i <= N:
        
    dp[N] = 1
    while i <= number:
        dp [i] = dp[i-1]+2
        if i%N > N//2:
            dp[i] = min(dp[i], (N-(i%N))*2+(i//N)+1)
        
        ones = int('1'*(i//10+1))
        if i//10+1 > 1 and ones <= i:
            dp[i] = min(dp[i], dp[i-ones]+i//10+1+1)
        print(i, dp[i])
        i += 1
    return dp[number]

print(solution(5, 12))