import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    
    k = 1
    while k < n:
        r, kk = rank, k
        sa.sort(key=lambda i: (r[i], r[i+kk] if i+kk < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            p, c = sa[i-1], sa[i]
            pp = (r[p], r[p+kk] if p+kk < n else -1)
            cc = (r[c], r[c+kk] if c+kk < n else -1)
            tmp[c] = tmp[p] + (1 if pp < cc else 0)
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k *= 2
    
    rank_inv = [0] * n
    for i in range(n):
        rank_inv[sa[i]] = i
    
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank_inv[i] > 0:
            j = sa[rank_inv[i] - 1]
            while i + h < n and j + h < n and s[i+h] == s[j+h]:
                h += 1
            lcp[rank_inv[i]] = h
            if h > 0:
                h -= 1
    
    best_val, best_start, best_len = 0, 0, 1
    
    for i in range(n):
        L = n - sa[i]
        if L > best_val:
            best_val, best_start, best_len = L, sa[i], L
    
    stack = []
    for i in range(1, n + 1):
        h_cur = lcp[i] if i < n else 0
        start = i
        while stack and stack[-1][0] >= h_cur:
            height, idx = stack.pop()
            val = height * (i - idx + 1)
            if val > best_val:
                best_val, best_start, best_len = val, sa[idx], height
            start = idx
        stack.append((h_cur, start))
    
    print(s[best_start:best_start + best_len])

solve()
