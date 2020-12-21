#!/usr/bin/env python3

with open('input') as f:
    numbers = [int(n) for n in f.readline().strip().split(',')]

turns, last = {n:i for i, n in enumerate(numbers[:-1])}, numbers[-1]

for t in range(len(turns) + 1, 30000000):
    turns[last], last = t - 1, t - 1 - turns[last] if last in turns else 0

print(last)
