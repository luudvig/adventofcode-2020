#!/usr/bin/env python3

from re import fullmatch

with open('input') as f:
    lines, mask, mem = f.read().splitlines(), None, {}

for l in lines:
    if l.startswith('mask'):
        mask = fullmatch('mask = ([0|1|X]+)', l).group(1)
    else:
        match = fullmatch('mem\[([0-9]+)\] = ([0-9]+)', l)
        value = ''.join([c if mask[i] == 'X' else mask[i] for i, c in enumerate(format(int(match.group(2)), '036b'))])
        mem[int(match.group(1))] = int(value, 2)

print(sum(mem.values()))
