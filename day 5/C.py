import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    
    for _ in range(T):
        n, m = int(data[idx]), int(data[idx+1]); idx += 2
        
        c = []
        for i in range(n):
            row = [0] + [int(data[idx+j]) for j in range(m)]
            idx += m
            c.append(row)
        
        dp = [0] * (m + 1)
        
        for i in range(n):
            new_dp = [0] * (m + 1)
            for j in range(m + 1):
                for invest in range(j + 1):
                    val = dp[j - invest] + c[i][invest]
                    if val > new_dp[j]:
                        new_dp[j] = val
            dp = new_dp
        
        print(dp[m])

solve()
