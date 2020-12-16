#!/usr/bin/env python3

with open('input') as f:
    adapters, differences = sorted([0] + list(map(int, f.readlines()))), {}

for i, a in enumerate(adapters[1:], 1):
    d = a - adapters[i - 1]
    differences[d] = differences.get(d, 0) + 1

print(differences[1] * (differences[3] + 1))
