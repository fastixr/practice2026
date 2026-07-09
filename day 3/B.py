import sys

def solve():
    data = sys.stdin.readline().split()
    l, r = int(data[0]), int(data[1])
    MOD = 10**9 + 7
    
    dp = [0] * (r + 1)
    dp[1] = 1
    
    for i in range(1, r + 1):
        v = dp[i]
        if v == 0:
            continue
        j = i + i
        while j <= r:
            dp[j] += v
            if dp[j] >= MOD:
                dp[j] -= MOD
            j += i
    
    result = 0
    for i in range(l, r + 1):
        result += dp[i]
    print(result % MOD)

solve()
