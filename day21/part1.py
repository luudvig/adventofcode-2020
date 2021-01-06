#!/usr/bin/env python3

from collections import Counter
from re import fullmatch

with open('input') as f:
    aller, ingr, foods = {}, Counter(), f.read().splitlines()

for f in foods:
    match = fullmatch('(.*) \(contains (.*)\)', f)
    i = set(match.group(1).split())
    for a in match.group(2).split(', '):
        aller[a] = aller.get(a, i).intersection(i)
    ingr.update(i)

for i in set().union(*aller.values()):
    del ingr[i]

print(sum(ingr.values()))
