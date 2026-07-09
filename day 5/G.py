import sys

INF = 10**18 + 5

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1

A = [int(data[index + i]) for i in range(n)]
index += n
B = [int(data[index + i]) for i in range(n)]
index += n
C = [int(data[index + i]) for i in range(n)]
index += n

m = int(data[index])
index += 1

queries = []
for _ in range(m):
    alpha = int(data[index])
    beta = int(data[index + 1])
    gamma = int(data[index + 2])
    queries.append((alpha, beta))
    index += 3

dp = [[-INF] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    a_val = A[i]
    b_val = B[i]
    c_val = C[i]
    new_dp = [[-INF] * (n + 1) for _ in range(n + 1)]
    for j in range(i + 1):
        for k in range(i - j + 1):
            val = dp[j][k]
            if val == -INF:
                continue
            if j + 1 <= n:
                new_dp[j + 1][k] = max(new_dp[j + 1][k], val + a_val)
            if k + 1 <= n:
                new_dp[j][k + 1] = max(new_dp[j][k + 1], val + b_val)
            new_dp[j][k] = max(new_dp[j][k], val + c_val)
    dp = new_dp

ans_list = []
for alpha, beta in queries:
    val = dp[alpha][beta]
    ans_list.append(str(val))

print('\n'.join(ans_list))
