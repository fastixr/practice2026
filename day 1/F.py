import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    parent = [0] * (n + 1)
    p = list(map(int, input().split()))
    for i, pi in enumerate(p, 2):
        parent[i] = pi
    s = input().strip()
    
    score = [0] * (n + 1)
    for i in range(1, n + 1):
        score[i] = 1 if s[i-1] == 'B' else -1
    
    for i in range(n, 1, -1):
        score[parent[i]] += score[i]
    
    print(sum(1 for i in range(1, n+1) if score[i] == 0))

t = int(input())
for _ in range(t):
    solve()
