import sys
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    words = data[1:1+n]
    
    total_len = sum(len(w) for w in words)
    
    children = {}
    node_count = 1
    
    MAX_ENTRIES = total_len + n + 10
    ll_val  = array('i', [0] * MAX_ENTRIES)
    ll_next = array('i', [-1] * MAX_ENTRIES)
    ll_cnt  = 0
    
    head = {}
    
    parent   = array('i', range(n))
    max_len  = array('i', [0] * n)
    comp_size = array('i', [0] * n)
    
    total_sum = 0
    out = []
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    for i in range(n):
        s = words[i]
        L = len(s)
        parent[i] = i
        max_len[i] = L
        comp_size[i] = 1
        total_sum += L
        
        node = 0
        path = [0]
        for b in s:
            key = node * 26 + b - 97
            nxt = children.get(key, -1)
            if nxt == -1:
                nxt = node_count
                children[key] = nxt
                node_count += 1
            node = nxt
            path.append(node)
        
        end_node = node
        cur_root = find(i)
        
        seen = set()
        e = head.get(end_node, -1)
        while e != -1:
            rf = find(ll_val[e])
            if rf != cur_root and rf not in seen:
                seen.add(rf)
                total_sum -= max_len[cur_root] * comp_size[cur_root] + max_len[rf] * comp_size[rf]
                parent[rf] = cur_root
                if max_len[rf] > max_len[cur_root]:
                    max_len[cur_root] = max_len[rf]
                comp_size[cur_root] += comp_size[rf]
                total_sum += max_len[cur_root] * comp_size[cur_root]
                cur_root = find(cur_root)
            e = ll_next[e]
        
        ll_val[ll_cnt] = cur_root
        ll_next[ll_cnt] = -1
        head[end_node] = ll_cnt
        ll_cnt += 1
        
        for j in range(len(path) - 2, -1, -1):
            anc = path[j]
            ll_val[ll_cnt] = cur_root
            ll_next[ll_cnt] = head.get(anc, -1)
            head[anc] = ll_cnt
            ll_cnt += 1
        
        out.append(total_sum)
    
    sys.stdout.write('\n'.join(map(str, out)) + '\n')

main()
