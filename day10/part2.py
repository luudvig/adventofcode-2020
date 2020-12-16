#!/usr/bin/env python3

with open('input') as f:
    adapters = sorted([0] + list(map(int, f.readlines())))
    adapters.append(adapters[-1] + 3)

def find_arrangements(i, m={}):
    a = 1 if i == len(adapters) - 1 else m.get(i, 0)
    if a == 0:
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] > 3:
                break
            a = a + find_arrangements(j, m)
        m[i] = a
    return a

print(find_arrangements(adapters[0]))
