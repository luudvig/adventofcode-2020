#!/usr/bin/env python3

from re import fullmatch

with open('input') as f:
    lines = [' '.join(sorted(l.split())) for l in f.read().split('\n\n')]

re = ('byr:(19[2-9][0-9]|200[0-2]) (cid:\S+ )?ecl:(amb|blu|brn|gry|grn|hzl|oth) eyr:20(2[0-9]|30) ' +
    'hcl:#[a-f0-9]{6} hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in) iyr:20(1[0-9]|20) pid:[0-9]{9}')

valid = [l for l in lines if fullmatch(re, l)]
print(len(valid))
