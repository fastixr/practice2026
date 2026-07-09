import sys
input = sys.stdin.readline

def solve():
    n, c, d = map(int, input().split())
    b = sorted(map(int, input().split()))
    
    a11 = b[0]
    expected = []
    for i in range(n):
        for j in range(n):
            expected.append(a11 + i*c + j*d)
    expected.sort()
    
    print("YES" if expected == b else "NO")

t = int(input())
for _ in range(t):
    solve()
