#!/usr/bin/env python3

def get_parents(child, result=set()):
    for p, c in rules.items():
        if child in c:
            result.add(p)
            get_parents(p, result)
    return result

with open('input') as f:
    rules = {' '.join(l.split()[:2]):[' '.join(c.split()[1:3]) for c in l.split('contain')[1].split(',')]
        for l in f.read().splitlines()}

print(len(get_parents('shiny gold')))
