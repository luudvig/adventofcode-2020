#!/usr/bin/env python3

with open('input') as f:
    cups, m = [int(l) for l in f.readline().strip()], 0

while m < 100:
    dest, m, pick = cups[0] - 1 if cups[0] > 1 else 9, m + 1, cups[1:4]

    while dest in pick:
        dest = dest - 1 if dest - 1 > 0 else 9

    if cups.index(dest) != 0:
        cups = [cups[0]] + cups[4:cups.index(dest) + 1] + pick + cups[cups.index(dest) + 1:]
    cups = cups[1:] + [cups[0]]

cups = cups[cups.index(1):] + cups[:cups.index(1)]
print(''.join([str(c) for c in cups[1:]]))
