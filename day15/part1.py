#!/usr/bin/env python3

with open('input') as f:
    turns = [int(n) for n in f.readline().strip().split(',')]

for t in range(len(turns), 2020):
    prev = next((i for i in reversed(range(len(turns) - 1)) if turns[i] == turns[-1]), -1)
    turns.append(t - 1 - prev) if prev != -1 else turns.append(0)

print(turns[-1])
