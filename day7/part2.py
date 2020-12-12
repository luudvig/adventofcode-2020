#!/usr/bin/env python3

def get_children(parent, result=[]):
    result.extend([get_children(c, result) for c in rules[parent]])
    return result

with open('input') as f:
    rules, lines = {}, f.read().splitlines()

for l in lines:
    for c in l.split('contain')[1].split(','):
        rules.setdefault(' '.join(l.split()[:2]), []).extend([] if 'no other bags' in c
            else [' '.join(c.split()[1:3])] * int(c.split()[0]))

print(len(get_children('shiny gold')))
