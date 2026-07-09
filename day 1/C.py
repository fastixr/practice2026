t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in range(n):
        res.append(i + 1)
        res.append(n + 2*i + 1)
        res.append(n + 2*i + 2)
    print(*res)
