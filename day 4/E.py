import sys
input = sys.stdin.readline

def solve(n):
    ns = str(n)
    ln = len(ns)
    results = []
    
    for a in range(1, 10001):
        ls = ln * a
        b_min = max(1, ls - 7)
        b_max = min(10000, n * a)
        
        if b_min > b_max:
            continue
        
        s = ns * a
        
        for b in range(b_min, b_max + 1):
            real_ans = n * a - b
            if real_ans < 0:
                break
            remaining = ls - b
            if remaining <= 0:
                break
            if int(s[:remaining]) == real_ans:
                results.append((a, b))
    
    return results

t = int(input())
for _ in range(t):
    n = int(input())
    res = solve(n)
    print(len(res))
    for a, b in res:
        print(a, b)
