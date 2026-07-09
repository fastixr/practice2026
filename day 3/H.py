import sys
import math

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    segs = []
    for _ in range(n):
        xa, ya, xb, yb = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        segs.append(((xa, ya), (xb, yb)))
    
    def dist(p1, p2):
        return math.hypot(p1[0]-p2[0], p1[1]-p2[1])
    
    INF = float('inf')
    a, b = segs[0]
    L = dist(a, b)
    dp = [L, L]
    prev = [a, b]
    
    for i in range(1, n):
        a2, b2 = segs[i]
        L2 = dist(a2, b2)
        new_dp = [INF, INF]
        for j in range(2):
            for k in range(2):
                start = a2 if k == 0 else b2
                end   = b2 if k == 0 else a2
                cost = dp[j] + dist(prev[j], start) + L2
                eidx = 0 if end == a2 else 1
                if cost < new_dp[eidx]:
                    new_dp[eidx] = cost
        dp = new_dp
        prev = [a2, b2]
    
    print(f"{min(dp):.7f}")

solve()
