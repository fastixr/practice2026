import sys
input = sys.stdin.readline

def meow_fast(n):
    MOD = 10**9 + 7
    MAXN = 2*n + 5
    fact = [1] * MAXN
    for i in range(1, MAXN):
        fact[i] = fact[i-1] * i % MOD
    inv_fact = [1] * MAXN
    inv_fact[MAXN-1] = pow(fact[MAXN-1], MOD-2, MOD)
    for i in range(MAXN-2, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    def C(a, b):
        if b < 0 or b > a: return 0
        return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD
    
    total = pow(2, n, MOD)
    
    for p in range(1, n+1):
        q = n - p
        prefix_q = [0] * (p + 1)
        s = 0
        for r in range(1, p + 1):
            s = (s + C(q, r-1)) % MOD
            prefix_q[r] = s
        
        cnt = pow(2, n, MOD)
        for j in range((p-1)//2 + 1):
            r = p - 2*j
            if r <= 0: break
            cnt = (cnt - C(p, j) * prefix_q[r]) % MOD
        
        total = (total + cnt) % MOD
    
    suffix = [0] * (n + 2)
    for k in range(n, -1, -1):
        suffix[k] = (suffix[k+1] + C(n, k)) % MOD
    
    for v in range(n+2, 2*n+2):
        k_min = v // 2
        if k_min > n: break
        total = (total + suffix[k_min]) % MOD
    
    return total

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    out.append(meow_fast(n))
print('\n'.join(map(str, out)))
