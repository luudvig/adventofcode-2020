#!/usr/bin/env python3

from re import fullmatch

with open ('input') as f:
    lines = f.read().splitlines()

items = [dict(p1=int(m.group(1)), p2=int(m.group(2)), let=m.group(3), pas=m.group(4))
    for m in [fullmatch('([0-9]+)-([0-9]+) (.): ([a-z]+)', l) for l in lines]]

valid = [i for i in items if sum([i['pas'][p - 1:p] == i['let'] for p in [i['p1'], i['p2']]]) == 1]
print(len(valid))
