#!/usr/bin/env python3

from re import fullmatch

with open('input') as f:
    lines = [' '.join(sorted(l.split())) for l in f.read().split('\n\n')]

valid = [l for l in lines if fullmatch('byr:\S+ (cid:\S+ )?ecl:\S+ eyr:\S+ hcl:\S+ hgt:\S+ iyr:\S+ pid:\S+', l)]
print(len(valid))
