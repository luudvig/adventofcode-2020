#!/usr/bin/env python3

with open('input') as f:
    lines = f.read().splitlines()

pos, trees = 3, 0

for l in lines[1:]:
    trees = trees + 1 if l[pos:pos + 1] == '#' else trees
    pos = pos + 3 if pos < len(l) - 3 else pos + 3 - len(l)

print(trees)
