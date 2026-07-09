import sys

def solve():
    data = sys.stdin.read().split()
    n, k, m = int(data[0]), int(data[1]), int(data[2])
    MOD = 10**9 + 7
    
    dangerous = set()
    for i in range(m):
        dangerous.add(int(data[3 + i]))
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    window_sum = 1
    
    for i in range(1, n + 1):
        if i in dangerous:
            dp[i] = 0
        else:
            dp[i] = window_sum % MOD
        
        window_sum += dp[i]
        if i >= k:
            window_sum -= dp[i - k]
        window_sum %= MOD
    
    print(dp[n])

solve()
