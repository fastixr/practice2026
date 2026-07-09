import sys
from array import array

MOD = 10**9 + 7

def main():
    input = sys.stdin.buffer.readline
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    k = int(line[2])
    
    M1 = m + 1
    danger = bytearray((n + 1) * M1)
    
    for _ in range(k):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        if 0 <= x <= n and 0 <= y <= m:
            danger[x * M1 + y] = 1
    
    if danger[0] or danger[n * M1 + m]:
        print(0)
        return
    
    dp = array('l', [0] * M1)
    dp[0] = 1
    
    for i in range(n + 1):
        base = i * M1
        for j in range(M1):
            if i == 0 and j == 0:
                continue
            if danger[base + j]:
                dp[j] = 0
                continue
            val = 0
            if j > 0:
                val = (val + dp[j - 1]) % MOD
            if i > 0:
                val = (val + dp[j]) % MOD
            dp[j] = val
    
    print(dp[m])

if __name__ == "__main__":
    main()
