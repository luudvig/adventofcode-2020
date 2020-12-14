#!/usr/bin/env python3

def validate(l, s):
    for i, t1 in enumerate(l):
        for t2 in l[i + 1:]:
            if t1 + t2 == s:
                return True
    return False

with open('input') as f:
    i, numbers = 25, list(map(int, f.readlines()))

while validate(numbers[i - 25:i], numbers[i]):
    i = i + 1

print(numbers[i])
