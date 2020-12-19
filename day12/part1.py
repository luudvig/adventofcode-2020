#!/usr/bin/env python3

from operator import add, sub

with open('input') as f:
    instr, ship = f.read().splitlines(), dict(x=0, y=0, d=90)

for i in instr:
    act, val = i[:1], int(i[1:])

    if act in ('L', 'R'):
        d = {'L': sub, 'R': add}[act](ship['d'], val)
        ship['d'] = d + 360 if d < 0 else d - 360 if d >= 360 else d
    else:
        act = {0: 'N', 180: 'S', 90: 'E', 270: 'W'}[ship['d']] if act == 'F' else act
        axis = {'N': 'y', 'S': 'y', 'E': 'x', 'W': 'x'}[act]
        ship[axis] = {'N': add, 'S': sub, 'E': add, 'W': sub}[act](ship[axis], val)

print(abs(ship['x']) + abs(ship['y']))
