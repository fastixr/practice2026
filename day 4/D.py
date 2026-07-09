import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    a = input().strip()
    
    INF = float('inf')
    min_water = [INF] * (n + 2)
    min_water[0] = 0
    
    for i in range(n + 1):
        w = min_water[i]
        if w == INF:
            continue
        
        is_surface = (i == 0) or (a[i-1] == 'L')
        
        if is_surface:
            for jump in range(1, m + 1):
                j = i + jump
                if j > n + 1:
                    break
                if j <= n and a[j-1] == 'C':
                    continue
                if w < min_water[j]:
                    min_water[j] = w
        else:
            j = i + 1
            if j <= n + 1 and (j == n + 1 or a[j-1] != 'C'):
                new_w = w + 1
                if new_w < min_water[j]:
                    min_water[j] = new_w
    
    print('YES' if min_water[n + 1] <= k else 'NO')

t = int(input())
for _ in range(t):
    solve()
