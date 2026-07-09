import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    front = (k + 1) // 2
    back = k // 2
    
    sunk = 0
    lo, hi = 0, n - 1
    
    while lo <= hi and front > 0:
        if a[lo] <= front:
            front -= a[lo]
            a[lo] = 0
            sunk += 1
            lo += 1
        else:
            a[lo] -= front
            front = 0
    
    while hi >= lo and back > 0:
        if a[hi] <= back:
            back -= a[hi]
            a[hi] = 0
            sunk += 1
            hi -= 1
        else:
            a[hi] -= back
            back = 0
    
    print(sunk)

t = int(input())
for _ in range(t):
    solve()
