#!/usr/bin/env python3

from itertools import product

def cycle(c):
    n = len(d & set(product(*[range(i - 1, i + 2) for i in c])))
    return n == 3 or (n == 4 and c in d)

with open('input') as f:
    d = {(x, y, 0, 0) for y, l in enumerate(f.readlines()) for x, c in enumerate(l) if c == '#'}

for i in range(6):
    d = set(filter(cycle, product(range(-i - 1, i + 8), repeat=4)))

print(len(d))
