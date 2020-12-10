#!/usr/bin/env python3

from re import fullmatch

with open ('input') as f:
    lines = f.read().splitlines()

items = [dict(min=int(m.group(1)), max=int(m.group(2)), let=m.group(3), pas=m.group(4))
    for m in [fullmatch('([0-9]+)-([0-9]+) (.): ([a-z]+)', l) for l in lines]]

valid = [i for i in items if i['pas'].count(i['let']) in range(i['min'], i['max'] + 1)]
print(len(valid))
