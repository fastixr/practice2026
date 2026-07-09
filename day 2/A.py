import sys
input = sys.stdin.readline

def solve():
    real = input().strip()
    dream = input().strip()
    n = len(real)
    
    if len(dream) != n:
        print(-1)
        return
    
    if sorted(real) != sorted(dream):
        print(-1)
        return
    
    doubled = real + real
    text = doubled[:2*n - 1] if n > 0 else doubled
    pattern = dream
    
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    positions = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    positions = [p for p in positions if p < n]
    
    if not positions:
        print(-1)
        return
    
    best_k = min((n - p) % n for p in positions)
    print(best_k)

solve()
