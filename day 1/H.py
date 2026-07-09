import sys
input = sys.stdin.readline

MOD = 676767677

def solve():
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    
    cnt = [0] * (m + 1)
    for x in b:
        cnt[x] += 1
    prefix = [0] * (m + 2)
    for t in range(1, m + 2):
        prefix[t] = prefix[t-1] + cnt[t-1]
    
    result = 1
    for i in range(n):
        t = b[i]
        if t == 0:
            continue
        t_nb = float('inf')
        if i > 0: t_nb = min(t_nb, b[i-1])
        if i < n-1: t_nb = min(t_nb, b[i+1])
        
        if t_nb >= t:
            print(0)
            return
        
        ct = prefix[t]
        if t_nb < t - 1:
            mult = ct - prefix[t-1]
        else:
            mult = ct
        
        if mult <= 0:
            print(0)
            return
        
        result = result * mult % MOD
    
    print(result)

t = int(input())
for _ in range(t):
    solve()
