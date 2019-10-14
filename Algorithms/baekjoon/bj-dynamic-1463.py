dp = [0, 0, 1, 1, 2]+[-1]*1000000

def make_one(n):
    if n < 4:
        return dp[n]
    i = 5
    while i <= n:
        dp[i] = dp[i-1]+1
        if i%2 == 0: dp[i] = min(dp[int(i/2)]+1, dp[i])
        if i%3 == 0: dp[i] = min(dp[int(i/3)]+1, dp[i])
        i += 1
    return dp[n]
    
x = int(input())
print(make_one(x))