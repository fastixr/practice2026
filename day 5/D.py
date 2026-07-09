import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1]); idx += 2
        a = [int(data[idx+i]) for i in range(n)]; idx += n
        
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            s = 0
            for j in range(i, 0, -1):
                s += a[j-1]
                if s <= k and dp[j-1] != INF:
                    if dp[j-1] + 1 < dp[i]:
                        dp[i] = dp[j-1] + 1
        
        print(dp[n] if dp[n] != INF else -1)

solve()
