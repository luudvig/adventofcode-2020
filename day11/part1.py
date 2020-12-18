#!/usr/bin/env python3

with open('input') as f:
    seat_pre, seat_cur = [], [[c for c in l] for l in f.read().splitlines()]

while seat_pre != seat_cur:
    seat_pre = [c.copy() for c in seat_cur]

    for y, r in enumerate(seat_pre):
        for x, c in enumerate(r):
            occ = 1 if x != 0 and r[x - 1] == '#' else 0
            occ = occ + 1 if x != len(r) - 1 and r[x + 1] == '#' else occ

            if y != 0:
                occ = occ + 1 if seat_pre[y - 1][x] == '#' else occ
                occ = occ + 1 if x != 0 and seat_pre[y - 1][x - 1] == '#' else occ
                occ = occ + 1 if x != len(r) - 1 and seat_pre[y - 1][x + 1] == '#' else occ

            if y != len(seat_pre) - 1:
                occ = occ + 1 if seat_pre[y + 1][x] == '#' else occ
                occ = occ + 1 if x != 0 and seat_pre[y + 1][x - 1] == '#' else occ
                occ = occ + 1 if x != len(r) - 1 and seat_pre[y + 1][x + 1] == '#' else occ

            seat_cur[y][x] = '#' if c == 'L' and occ == 0 else 'L' if c == '#' and occ > 3 else seat_cur[y][x]

print(len([c for r in seat_cur for c in r if c == '#']))
