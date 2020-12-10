#!/usr/bin/env python3

def find_terms(n, s):
    for i, t1 in enumerate(n):
        for t2 in n[i + 1:]:
            if t1 + t2 == s:
                return t1, t2

with open('input') as f:
    numbers = list(map(int, f.readlines()))

term1, term2 = find_terms(numbers, 2020)
print(term1 * term2)
