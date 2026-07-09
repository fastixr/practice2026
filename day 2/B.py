import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    fail = [0] * n
    
    for i in range(1, n):
        j = fail[i-1]
        while j > 0 and s[i] != s[j]:
            j = fail[j-1]
        if s[i] == s[j]:
            j += 1
        fail[i] = j
    
    k = n - fail[n-1]
    if n % k == 0:
        print(k)
    else:
        print(n)

solve()
