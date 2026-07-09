import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
D = list(map(int, data[1:]))

kill = [0] * n
for i in range(n):
    kill[i] = (1 << i) | (1 << ((i-2) % n)) | (1 << ((i+2) % n))

FULL = (1 << n) - 1

dp = [float('inf')] * (1 << n)
dp[0] = 0

sum_d = [0] * (1 << n)
for mask in range(1 << n):
    s = 0
    for j in range(n):
        if mask & (1 << j):
            s += D[j]
    sum_d[mask] = s

for mask in range(1, 1 << n):
    for shot in range(n):
        killed = kill[shot] & mask
        new_mask = mask ^ killed
        cost = sum_d[new_mask]
        dp[mask] = min(dp[mask], cost + dp[new_mask])

ans = dp[FULL] + 1
print(int(ans))
