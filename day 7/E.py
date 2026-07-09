import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    a = [int(c) for c in s]
    
    for k in range(n, 0, -1):
        flip = [0] * (n + 1)
        cur = 0
        ok = True
        for i in range(n):
            cur += flip[i]
            val = (a[i] + cur) % 2
            if val == 0:
                if i + k > n:
                    ok = False
                    break
                flip[i + k] -= 1
                cur += 1
        if ok:
            print(k)
            return

t = int(input())
for _ in range(t):
    solve()
