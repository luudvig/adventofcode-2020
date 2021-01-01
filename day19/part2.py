#!/usr/bin/env python3

from re import fullmatch

def get_regex(k, r=[]):
    if type(rules[k]) == str:
        r.append(rules[k])
    else:
        r.append('(')
        for i, v in enumerate(rules[k]):
            r.append('|') if i else r
            for n in v:
                get_regex(n, r)
        r.append(')')
    return r

with open('input') as f:
    line, rules = f.readline().split(':'), {}
    while len(line) > 1:
        k, v = line[0], line[1].strip()
        rules[int(k)] = v[1:2] if v.startswith('"') and v.endswith('"') else [[int(n) for n in p.split()] for p in v.split('|')]
        line = f.readline().split(':')
    messages = f.read().splitlines()

rules[8] = [[42], [42, 42], [42, 42, 42], [42, 42, 42, 42], [42, 42, 42, 42, 42]]
rules[11] = [[42, 31], [42, 42, 31, 31], [42, 42, 42, 31, 31, 31], [42, 42, 42, 42, 31, 31, 31, 31]] 

re = ''.join(get_regex(0))
matches = [m for m in messages if fullmatch(re, m)]
print(len(matches))
