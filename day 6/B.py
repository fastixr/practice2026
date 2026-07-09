import sys
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    
    if n == 1:
        print(0)
        return
    
    c = array('i', [int(x) for x in data[1:1+n*n]])
    
    INF = 10**8
    half = 1 << (n - 1)
    dp = array('i', [INF] * (half * n))
    dp[0] = 0
    
    for mask in range(1, 1 << n):
        if not (mask & 1):
            continue
        mask_idx = mask >> 1
        base = mask_idx * n
        for u in range(n):
            val = dp[base + u]
            if val >= INF or not (mask >> u) & 1:
                continue
            cu_base = u * n
            for v in range(n):
                if (mask >> v) & 1:
                    continue
                new_val = val + c[cu_base + v]
                new_idx = ((mask | (1 << v)) >> 1) * n + v
                if new_val < dp[new_idx]:
                    dp[new_idx] = new_val
    
    full_idx = ((1 << n) - 1) >> 1
    base = full_idx * n
    ans = INF
    for u in range(n):
        val = dp[base + u]
        if val < INF:
            total = val + c[u * n]
            if total < ans:
                ans = total
    
    print(ans)

main()
