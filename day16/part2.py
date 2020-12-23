#!/usr/bin/env python3

from functools import reduce
from re import match

with open('input') as f:
    line, rules = f.readline().strip(), {}
    while line != '':
        m = match('(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line)
        rules[m.group(1)] = [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]
        line = f.readline().strip()

    while line != 'your ticket:':
        line = f.readline().strip()

    ticket = [int(p) for p in f.readline().strip().split(',')]

    while line != 'nearby tickets:':
        line = f.readline().strip()

    line, nearby = f.readline().strip(), []
    while line != '':
        nearby.append([int(p) for p in line.split(',')])
        line = f.readline().strip()

for n in nearby.copy():
    for p in n:
        if any(l <= p <= h for (l, h) in [t for r in rules.values() for t in r]):
            continue
        nearby.remove(n)
        break

columns = {}
while rules:
    for i, c in enumerate(zip(*nearby)):
        valid = [n for n, r in rules.items() if all(any(l <= p <= h for (l, h) in r) for p in c)]
        if len(valid) == 1:
            columns[i] = valid[0]
            del rules[valid[0]]

values = [p for i, p in enumerate(ticket) if columns[i].startswith('departure')]
print(reduce(lambda v1, v2: v1 * v2, values))
