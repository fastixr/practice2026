import sys

def main():
    data = sys.stdin.read().split()
    MOD = 10**9 + 7
    MAX_N = 100
    MAX_S = 1000
    
    g = [[0] * (MAX_S + 1) for _ in range(MAX_N + 1)]
    g[0][0] = 1
    for i in range(1, MAX_N + 1):
        for j in range(MAX_S + 1):
            for d in range(min(10, j + 1)):
                g[i][j] = (g[i][j] + g[i-1][j-d]) % MOD
    
    t = int(data[0])
    out = []
    for i in range(t):
        n, s = int(data[1 + 2*i]), int(data[2 + 2*i])
        out.append(g[n][s])
    
    print('\n'.join(map(str, out)))

main()
