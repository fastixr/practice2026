import sys

MOD = 10**9 + 7
N = int(sys.stdin.read().strip())

dp = [0] * (N + 1)
dp[0] = 1

for num in range(1, N + 1):
    for s in range(N, num - 1, -1):
        dp[s] = (dp[s] + dp[s - num]) % MOD

print(dp[N])
