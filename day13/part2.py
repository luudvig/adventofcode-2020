#!/usr/bin/env python3

from itertools import count

with open('input') as f:
    time, step, buses = 0, 1, {i:int(b) for i, b in enumerate(f.read().splitlines()[1].split(',')) if b != 'x'}

for i, b in buses.items():
    time, step = next(t for t in count(time, step) if (t + i) % b == 0), step * b

print(time)
