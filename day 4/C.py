import sys
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    big    = list(range(n, k-1, -1))
    middle = list(range(k-1, m, -1))
    small  = list(range(1, m+1))
    print(*big, *middle, *small)

t = int(input())
for _ in range(t):
    solve()
