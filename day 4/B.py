import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    base = max(a)
    a.remove(base)
    
    total = 0
    for x in a:
        total += 1 if x == 1 else 2*x - 1
    
    print(total)

t = int(input())
for _ in range(t):
    solve()
