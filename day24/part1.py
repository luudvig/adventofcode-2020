#!/usr/bin/env python3

with open('input') as f:
    black, lines = set(), f.read().splitlines()

for l in lines:
    x, y, z = 0, 0, 0

    while l:
        if l.startswith('e'):
            l, x, y = l[1:], x + 1, y - 1
        elif l.startswith('se'):
            l, y, z = l[2:], y - 1, z + 1
        elif l.startswith('sw'):
            l, x, z = l[2:], x - 1, z + 1
        elif l.startswith('w'):
            l, x, y = l[1:], x - 1, y + 1
        elif l.startswith('nw'):
            l, z, y = l[2:], z - 1, y + 1
        elif l.startswith('ne'):
            l, x, z = l[2:], x + 1, z - 1

    black.add((x, y, z)) if (x, y, z) not in black else black.remove((x, y, z))

print(len(black))
