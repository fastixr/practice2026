t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    pair = min(b, 2*a)
    print((n//2)*pair + (n%2)*a)
