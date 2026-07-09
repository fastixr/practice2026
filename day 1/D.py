def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]
 
primes = sieve(200000)
 
t = int(input())
for _ in range(t):
    n = int(input())
    res = [primes[i] * primes[i+1] for i in range(n)]
    print(*res)
