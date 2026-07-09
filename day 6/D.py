import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
index = 1
adj = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        adj[i][j] = int(data[index])
        index += 1

dp = [[0] * n for _ in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = 1

for mask in range(1 << n):
    for last in range(n):
        if dp[mask][last] == 0:
            continue
        for next in range(n):
            if (mask & (1 << next)) == 0 and adj[last][next]:
                new_mask = mask | (1 << next)
                dp[new_mask][next] += dp[mask][last]

ans = 0
full = (1 << n) - 1
for last in range(n):
    ans += dp[full][last]

print(ans)
