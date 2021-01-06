#!/usr/bin/env python3

from re import fullmatch

with open('input') as f:
    aller, foods = {}, f.read().splitlines()

for f in foods:
    match = fullmatch('(.*) \(contains (.*)\)', f)
    i = set(match.group(1).split())
    for a in match.group(2).split(', '):
        aller[a] = aller.get(a, i).intersection(i)

while any(len(v) > 1 for v in aller.values()):
    for i in set().union(*[v for v in aller.values() if len(v) == 1]):
        for a in [k for k, v in aller.items() if len(v) > 1]:
            aller[a].discard(i)

print(','.join([i for a in sorted(aller) for i in aller[a]]))
