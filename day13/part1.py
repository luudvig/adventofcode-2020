#!/usr/bin/env python3

from itertools import count

with open('input') as f:
    time, buses = int(f.readline().strip()), {int(b):None for b in f.readline().strip().split(',') if b != 'x'}

buses = {b:next(t for t in count(0, b) if t >= time) for b in buses}
print((min(buses.values()) - time) * min(buses, key=buses.get))
