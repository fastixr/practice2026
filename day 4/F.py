import sys
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    segments = 1
    S = {1}
    
    for v in a:
        if v > x or x % v != 0:
            continue
        
        new_S = set(S)
        for s in S:
            ns = s * v
            if x % ns == 0:
                new_S.add(ns)
        
        if x in new_S:
            segments += 1
            S = {1}
            if x % v == 0:
                S.add(v)
        else:
            S = new_S
    
    print(segments)

t = int(input())
for _ in range(t):
    solve()
