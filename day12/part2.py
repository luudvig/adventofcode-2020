#!/usr/bin/env python3

from operator import add, sub

with open('input') as f:
    instr, ship, wayp = f.read().splitlines(), dict(x=0, y=0), dict(x=10, y=1)

for i in instr:
    act, val = i[:1], int(i[1:])

    if act == 'F':
        ship['x'] = ship['x'] + wayp['x'] * val
        ship['y'] = ship['y'] + wayp['y'] * val
    elif act in ('L', 'R'):
        if val == 180:
            wayp['x'], wayp['y'] = wayp['x'] * -1, wayp['y'] * -1
        else:
            x, y = wayp['x'], wayp['y']
            wayp['x'] = y * -1 if (act == 'L' and val == 90) or (act == 'R' and val == 270) else y
            wayp['y'] = x * -1 if (act == 'R' and val == 90) or (act == 'L' and val == 270) else x
    else:
        axis = {'N': 'y', 'S': 'y', 'E': 'x', 'W': 'x'}[act]
        wayp[axis] = {'N': add, 'S': sub, 'E': add, 'W': sub}[act](wayp[axis], val)

print(abs(ship['x']) + abs(ship['y']))
