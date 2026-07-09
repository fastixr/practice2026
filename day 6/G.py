import sys

MOD = 998244353

data = sys.stdin.read().splitlines()
n, m = map(int, data[0].split())
grid = data[1:1 + n]

if m > n:
    new_grid = [''.join(grid[i][j] for i in range(n)) for j in range(m)]
    grid = new_grid
    n, m = m, n

dp = [0] * (1 << m)
dp[0] = 1

for i in range(n):
    row = grid[i]
    row_free = [row[j] == '.' for j in range(m)]
    new_dp = [0] * (1 << m)
    for in_mask in range(1 << m):
        if dp[in_mask] == 0:
            continue
        def dfs(c, out_mask):
            if c == m:
                new_dp[out_mask] = (new_dp[out_mask] + dp[in_mask]) % MOD
                return
            if (in_mask & (1 << c)):
                if not row_free[c]:
                    return
                dfs(c + 1, out_mask)
                return
            if not row_free[c]:
                dfs(c + 1, out_mask)
                return
            dfs(c + 1, out_mask | (1 << c))
            if c + 1 < m and not (in_mask & (1 << (c + 1))) and row_free[c + 1]:
                dfs(c + 2, out_mask)
        dfs(0, 0)
    dp = new_dp

print(dp[0])
