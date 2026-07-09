import sys

MOD = 998244353

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
x = int(data[index])
index += 1

A = []
total = 1
max_sum = 0
for i in range(n):
    ai = int(data[index])
    index += 1
    A.append(ai)
    total = (total * ai) % MOD
    max_sum += ai

dp = [0] * (max_sum + 1)
dp[0] = 1

for ai in A:
    cum = [0] * (max_sum + 2)
    for s in range(max_sum + 1):
        cum[s + 1] = (cum[s] + dp[s]) % MOD
    new_dp = [0] * (max_sum + 1)
    for t in range(1, max_sum + 1):
        left = max(0, t - ai)
        new_dp[t] = (cum[t] - cum[left] + MOD) % MOD
    dp = new_dp

favorable = 0
for s in range(x, max_sum + 1):
    favorable = (favorable + dp[s]) % MOD

inv_total = pow(total, MOD - 2, MOD)
ans = favorable * inv_total % MOD
print(ans)
