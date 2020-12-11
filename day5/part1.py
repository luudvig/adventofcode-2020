#!/usr/bin/env python3

with open('input') as f:
    lines = sorted(f.read().splitlines())

p = [l for l in lines if l[:7] == lines[0][:7]][-1]
r, c = range(128), range(8)

for l in p[:7]:
    r = r[:len(r)//2] if l == 'F' else r[len(r)//2:]

for l in p[7:]:
    c = c[:len(c)//2] if l == 'L' else c[len(c)//2:]

print(r[0] * 8 + c[0])
