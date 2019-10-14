dp = [0, 0, 1, 1, 2]+[-1]*1000000

def make_one(n):
    i = 1
    while i <= n:
        dp[i] = dp[i-1]+1
        if n%2 == 0: dp[i] = min(dp[i/2]+1, dp[i])
        if n%3 == 0: dp[i] = min(dp[i/3]+1, dp[i])
        i += 1
    return dp[n]
    
x = int(input())
print(make_one(x))