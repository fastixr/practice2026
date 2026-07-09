import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 2:
        print(a[0] ^ a[1])
        return
    
    BITS = 30
    trie = {}
    best = 0
    
    for x in a:
        node = trie
        cur = 0
        for bit in range(BITS - 1, -1, -1):
            b = (x >> bit) & 1
            want = 1 - b
            if want in node:
                cur |= (1 << bit)
                node = node[want]
            elif b in node:
                node = node[b]
            else:
                break
        best = max(best, cur)
        node = trie
        for bit in range(BITS - 1, -1, -1):
            b = (x >> bit) & 1
            if b not in node:
                node[b] = {}
            node = node[b]
    
    print(best)
 
t = int(input())
for _ in range(t):
    solve()
