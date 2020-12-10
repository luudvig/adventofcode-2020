#!/usr/bin/env python3

from functools import reduce

with open('input') as f:
    lines = f.read().splitlines()

factors, slopes = [], [
    {'r': 1, 'd': 1},
    {'r': 3, 'd': 1},
    {'r': 5, 'd': 1},
    {'r': 7, 'd': 1},
    {'r': 1, 'd': 2}
]

for s in slopes:
    pos, trees = s['r'], 0

    for i in range(s['d'], len(lines), s['d']):
        l = lines[i]
        trees = trees + 1 if l[pos:pos + 1] == '#' else trees
        pos = pos + s['r'] if pos < len(l) - s['r'] else pos + s['r'] - len(l)

    factors.append(trees)

print(reduce(lambda f1, f2: f1 * f2, factors))
