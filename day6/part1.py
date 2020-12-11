#!/usr/bin/env python3

with open('input') as f:
    groups = f.read().split('\n\n')

counts = [len(set(g.replace('\n', ''))) for g in groups]
print(sum(counts))
