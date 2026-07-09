import sys

def solve():
    s = sys.stdin.readline().strip()
    t = s + '#' + s[::-1]
    n = len(t)
    fail = [0] * n
    
    for i in range(1, n):
        j = fail[i-1]
        while j > 0 and t[i] != t[j]:
            j = fail[j-1]
        if t[i] == t[j]:
            j += 1
        fail[i] = j
    
    print(fail[-1])

solve()
