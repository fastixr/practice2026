import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    triangle = []
    idx = 1
    for i in range(1, n+1):
        row = [int(data[idx+j]) for j in range(i)]
        idx += i
        triangle.append(row)
    
    dp = triangle[0][:]
    
    for i in range(1, n):
        new_dp = [0] * (i+1)
        for j in range(i+1):
            best = -1
            if j > 0:
                best = max(best, dp[j-1])
            if j < i:
                best = max(best, dp[j])
            new_dp[j] = triangle[i][j] + best
        dp = new_dp
    
    print(max(dp))

solve()
