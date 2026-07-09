import sys

def solve():
    n = int(sys.stdin.read())
    a = [0, 1, 1, 2, 4, 6]
    for i in range(6, n + 1):
        a.append(a[i-1] + a[i-2] - a[i-5])
    print(a[n])

solve()
