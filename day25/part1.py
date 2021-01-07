#!/usr/bin/env python3

with open('input') as f:
    card, door = [int(l) for l in f.read().splitlines()]

loop, subject, value = 0, 7, 1

while door != value:
    value = (value * subject) % 20201227
    loop = loop + 1

for i in range(loop):
    value = (value * card if i else card) % 20201227

print(value)
