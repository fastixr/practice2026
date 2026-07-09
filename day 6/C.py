import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n, m, k = int(data[idx]), int(data[idx+1]), int(data[idx+2]); idx += 3
    
    edges = []
    for _ in range(m):
        u, v = int(data[idx])-1, int(data[idx+1])-1; idx += 2
        edges.append((u, v))
    
    best_prod = None
    best_assign = None
    
    pw = [3**i for i in range(n)]
    
    for mask in range(3**n):
        tmp = mask
        types = [0]*n
        for i in range(n):
            types[i] = tmp % 3
            tmp //= 3
        
        h = 0
        for i in range(n):
            t = types[i]
            if t == 2: h += 1
            elif t == 1: h -= 1
        
        p = 0
        for u, v in edges:
            tu, tv = types[u], types[v]
            if tu == 2:
                if tv == 0: h += 1
                elif tv == 1: h -= 1
            elif tv == 2:
                if tu == 0: h += 1
                elif tu == 1: h -= 1
            if tu == 1 and tv == 0: p += 1
            elif tu == 0 and tv == 1: p += 1
        
        if h >= k and (best_prod is None or p > best_prod):
            best_prod = p
            best_assign = types[:]
    
    print(best_prod)
    
    res = [[], [], []]
    for i, t in enumerate(best_assign):
        res[t].append(i+1)
    
    for lst in res:
        print(len(lst), *lst)

main()
