import sys
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    g = math.gcd(a[0][0], a[-1][-1])

    divs = []
    i = 1
    while i * i <= g:
        if g % i == 0:
            divs.append(i)
            if i * i != g:
                divs.append(g // i)
        i += 1
    divs.sort(reverse=True)

    for d in divs:
        dp = [[False] * m for _ in range(n)]

        if a[0][0] % d != 0:
            continue

        dp[0][0] = True

        for i in range(n):
            for j in range(m):
                if a[i][j] % d != 0:
                    continue
                if i == 0 and j == 0:
                    continue
                if i > 0 and dp[i - 1][j]:
                    dp[i][j] = True
                elif j > 0 and dp[i][j - 1]:
                    dp[i][j] = True

        if dp[n - 1][m - 1]:
            print(d)
            break
