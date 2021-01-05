#!/usr/bin/env python3

from collections import Counter

def get_edges(tile):
    return [tile[0], ''.join(reversed(tile[-1])), ''.join(l[-1] for l in tile), ''.join(l[0] for l in reversed(tile))]

with open('input') as f:
    tiles = {int(p.partition('\n')[0][5:-1]): p.splitlines()[1:] for p in f.read().split('\n\n') if p}

corners, edges = [], Counter()

for t in tiles.values():
    edges.update(get_edges(t))
    edges.update(get_edges(t[::-1]))

for i, t in tiles.items():
    unique = [e for e in get_edges(t) if edges[e] == 1]
    corners.append(i) if len(unique) == 2 else corners

print(corners[0] * corners[1] * corners[2] * corners[3])
