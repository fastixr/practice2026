import sys
from array import array

def solve():
    n = int(sys.stdin.buffer.read())
    
    dp = array('i', [0] * (n + 1))
    
    for i in range(2, n + 1):
        best = dp[i-1] + i
        if i % 2 == 0:
            v = dp[i//2] + i
            if v < best: best = v
        if i % 3 == 0:
            v = dp[i//3] + i
            if v < best: best = v
        dp[i] = best
    
    print(dp[n])

solve()
