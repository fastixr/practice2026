t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    best = 0
    for i in range(6):
        for j in range(6 - i):
            k = 5 - i - j
            best = max(best, (a+i)*(b+j)*(c+k))
    print(best)
