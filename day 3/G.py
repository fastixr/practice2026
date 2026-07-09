import sys

def solve():
    n, k = map(int, sys.stdin.read().split())
    MOD = 10**9 + 7
    
    def digit_mask(x):
        m = 0
        while x:
            m |= 1 << (x % 10)
            x //= 10
        return m
    
    mask_to_count = {}
    for v in range(1, k + 1):
        mv = digit_mask(v)
        mask_to_count[mv] = mask_to_count.get(mv, 0) + 1
    
    distinct_masks = list(mask_to_count.keys())
    
    compat = {m: [mu for mu in distinct_masks if mu & m == 0] for m in distinct_masks}
    
    mask_dp = dict(mask_to_count)
    
    for _ in range(n - 1):
        new_mask_dp = {}
        for mv in distinct_masks:
            s = sum(mask_dp.get(mu, 0) for mu in compat[mv]) % MOD
            if s:
                new_mask_dp[mv] = s * mask_to_count[mv] % MOD
        mask_dp = new_mask_dp
    
    print(sum(mask_dp.values()) % MOD)

solve()
