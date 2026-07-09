import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    
    grid = []
    for i in range(n):
        row = [int(data[idx+j]) for j in range(m)]
        idx += m
        grid.append(row)
    
    dp = [[-1] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            best = -1
            if i > 0 and dp[i-1][j] >= 0:
                best = max(best, dp[i-1][j])
            if j > 0 and dp[i][j-1] >= 0:
                best = max(best, dp[i][j-1])
            if i > 0 and j > 0 and dp[i-1][j-1] >= 0:
                best = max(best, dp[i-1][j-1])
            if best >= 0:
                dp[i][j] = best + grid[i][j]
    
    print(dp[n-1][m-1])

solve()
