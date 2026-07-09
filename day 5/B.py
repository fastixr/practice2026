import sys

def solve():
    n, k = map(int, sys.stdin.read().split())
    MOD = 10**9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    window = 1
    
    for i in range(1, n + 1):
        dp[i] = window % MOD
        window += dp[i]
        if i >= k:
            window -= dp[i - k]
        window %= MOD
    
    print(dp[n])

solve()
