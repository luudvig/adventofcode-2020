#!/usr/bin/env python3

def occupied(y, ye, ys, x, xe, xs):
    while y != ye and x != xe:
        if seat_pre[y][x] != '.':
            return True if seat_pre[y][x] == '#' else False
        y, x = y + ys, x + xs
    return False

with open('input') as f:
    seat_pre, seat_cur = [], [[c for c in l] for l in f.read().splitlines()]

while seat_pre != seat_cur:
    seat_pre = [c.copy() for c in seat_cur]

    for y, r in enumerate(seat_pre):
        for x, c in enumerate(r):
            occ = 1 if occupied(y - 1, -1, -1, x + 1, len(r), 1) else 0
            occ = occ + 1 if occupied(y + 1, len(seat_pre), 1, x + 1, len(r), 1) else occ
            occ = occ + 1 if occupied(y + 1, len(seat_pre), 1, x - 1, -1, -1) else occ
            occ = occ + 1 if occupied(y - 1, -1, -1, x - 1, -1, -1) else occ

            occ = occ + 1 if occupied(y, y + 1, 0, x - 1, -1, -1) else occ
            occ = occ + 1 if occupied(y, y + 1, 0, x + 1, len(r), 1) else occ

            occ = occ + 1 if occupied(y - 1, -1, -1, x, x + 1, 0) else occ
            occ = occ + 1 if occupied(y + 1, len(seat_pre), 1, x, x + 1, 0) else occ

            seat_cur[y][x] = '#' if c == 'L' and occ == 0 else 'L' if c == '#' and occ > 4 else seat_cur[y][x]

print(len([c for r in seat_cur for c in r if c == '#']))
