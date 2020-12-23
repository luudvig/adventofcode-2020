#!/usr/bin/env python3

from re import match

with open('input') as f:
    line, rules = f.readline().strip(), []
    while line != '':
        m = match('.*: ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)', line)
        rules.extend([(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))])
        line = f.readline().strip()

    while line != 'nearby tickets:':
        line = f.readline().strip()

    line, nearby = f.readline().strip(), []
    while line != '':
        nearby.extend([int(p) for p in line.split(',')])
        line = f.readline().strip()

invalid = [n for n in nearby if not any(l <= n <= h for (l, h) in rules)]
print(sum(invalid))
