#!/usr/bin/env python3

with open('input') as f:
    groups = f.read().split('\n\n')

counts = [len([a for a in set(g.replace('\n', '')) if g.count(a) == g.count('\n') + 1]) for g in groups]
print(sum(counts))
