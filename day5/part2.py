#!/usr/bin/env python3

def pas_to_seat(pas):
    r, c = range(128), range(8)

    for p in pas[:7]:
        r = r[:len(r)//2] if p == 'F' else r[len(r)//2:]

    for p in pas[7:]:
        c = c[:len(c)//2] if p == 'L' else c[len(c)//2:]

    return r[0] * 8 + c[0]

with open('input') as f:
    lines = f.read().splitlines()

occup = [pas_to_seat(l) for l in lines]
avail = [s for s in range(min(occup), max(occup) + 1) if s not in occup]

print(avail[0])
