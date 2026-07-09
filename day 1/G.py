import sys
input = sys.stdin.readline

def solve():
    x, y = map(int, input().split())
    n = x + y
    
    if x > y or (x == 0 and y % 2 == 0):
        print("NO")
        return
    
    print("YES")
    edges = []
    v = 2
    
    if n % 2 == 1:
        num_chains = x
        num_leaves = y - x - 1
    else:
        num_chains = x - 1
        num_leaves = y - x + 1
    
    for _ in range(num_chains):
        edges.append(f"1 {v}")
        edges.append(f"{v} {v+1}")
        v += 2
    
    for _ in range(num_leaves):
        edges.append(f"1 {v}")
        v += 1
    
    print('\n'.join(edges))

t = int(input())
for _ in range(t):
    solve()
