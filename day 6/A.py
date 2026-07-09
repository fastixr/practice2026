import sys
from itertools import combinations
from functools import reduce
from operator import xor

def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    a = [int(data[2+i]) for i in range(n)]
    
    best = 0
    for combo in combinations(a, k):
        val = reduce(xor, combo)
        if val > best:
            best = val
    print(best)

main()
