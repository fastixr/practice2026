import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1

a = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(data[index]))
        index += 1
    a.append(row)

dp = [[0] * M for _ in range(N)]
dp[0][0] = a[0][0]

moves = [(2, -1), (2, 1), (1, 2), (-1, 2)]

for s in range(N + M):
    for i in range(max(0, s - (M - 1)), min(s, N - 1) + 1):
        j = s - i
        if 0 <= j < M and dp[i][j] > 0 or (i == 0 and j == 0):
            for di, dj in moves:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    dp[ni][nj] = max(dp[ni][nj], dp[i][j] + a[ni][nj])

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dp[i][j])

print(ans)
