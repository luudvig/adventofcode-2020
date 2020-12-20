#!/usr/bin/env python3

from itertools import product
from re import finditer, fullmatch

def addresses(address):
    result, pos = [], [m.start() for m in finditer('X', address)]
    comb = product(('0', '1'), repeat=len(pos))
    for c in comb:
        addr = list(address)
        for i, p in enumerate(pos):
            addr[p] = c[i]
        result.append(''.join(addr))
    return result

with open('input') as f:
    lines, mask, mem = f.read().splitlines(), None, {}

for l in lines:
    if l.startswith('mask'):
        mask = fullmatch('mask = ([0|1|X]+)', l).group(1)
    else:
        match = fullmatch('mem\[([0-9]+)\] = ([0-9]+)', l)
        addr = ''.join([c if mask[i] == '0' else mask[i] for i, c in enumerate(format(int(match.group(1)), '036b'))])
        mem.update({int(a, 2):int(match.group(2)) for a in addresses(addr)})

print(sum(mem.values()))
