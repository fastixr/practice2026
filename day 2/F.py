import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]
    
    BITS = 30
    MAXNODES = n * (BITS + 1) + 10
    
    child0 = [-1] * MAXNODES
    child1 = [-1] * MAXNODES
    cnt = [0] * MAXNODES
    node_cnt = 1
    
    bits_order = tuple(range(BITS - 1, -1, -1))
    
    for x in a:
        node = 0
        cnt[0] += 1
        for bit in bits_order:
            if (x >> bit) & 1:
                nxt = child1[node]
                if nxt == -1:
                    nxt = node_cnt
                    child1[node] = nxt
                    node_cnt += 1
            else:
                nxt = child0[node]
                if nxt == -1:
                    nxt = node_cnt
                    child0[node] = nxt
                    node_cnt += 1
            node = nxt
            cnt[node] += 1
    
    out = []
    path = [0] * (BITS + 1)
    
    for x in a:
        node = 0
        cnt[0] -= 1
        path[0] = 0
        for idx, bit in enumerate(bits_order):
            node = child1[node] if (x >> bit) & 1 else child0[node]
            cnt[node] -= 1
            path[idx + 1] = node
        
        node = 0
        mn = 0
        for bit in bits_order:
            b = (x >> bit) & 1
            sc = child1[node] if b else child0[node]
            oc = child0[node] if b else child1[node]
            if sc != -1 and cnt[sc] > 0:
                node = sc
            else:
                mn |= (1 << bit)
                node = oc
        
        node = 0
        mx = 0
        for bit in bits_order:
            b = (x >> bit) & 1
            sc = child1[node] if b else child0[node]
            oc = child0[node] if b else child1[node]
            if oc != -1 and cnt[oc] > 0:
                mx |= (1 << bit)
                node = oc
            else:
                node = sc
        
        out.append(f"{mn} {mx}")
        
        for p in path:
            cnt[p] += 1
    
    sys.stdout.write('\n'.join(out) + '\n')

main()
