import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
x = int(data[1])
W = list(map(int, data[2:]))

mid = n // 2
first = W[:mid]
second = W[mid:]

from collections import defaultdict
sum_to_mask = {}
def gen_half(arr, start_idx):
    k = len(arr)
    for mask in range(1 << k):
        s = 0
        for j in range(k):
            if mask & (1 << j):
                s += arr[j]   # R +
            else:
                s -= arr[j]   # L -
        sum_to_mask[s] = (mask, start_idx)

gen_half(first, 0)

found = False
target_mask = None
sec_start = mid
for mask in range(1 << len(second)):
    s2 = 0
    for j in range(len(second)):
        if mask & (1 << j):
            s2 += second[j]
        else:
            s2 -= second[j]
    needed = x - s2
    if needed in sum_to_mask:
        found = True
        fmask, fstart = sum_to_mask[needed]
        target_mask = (fmask, mask)
        break

res = [''] * n
fmask, smask = target_mask
for j in range(len(first)):
    if fmask & (1 << j):
        res[j] = 'R'
    else:
        res[j] = 'L'
for j in range(len(second)):
    if smask & (1 << j):
        res[mid + j] = 'R'
    else:
        res[mid + j] = 'L'

print(''.join(res))
