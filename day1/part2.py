#!/usr/bin/env python3

def find_terms(n1, s):
    for i1, t1 in enumerate(n1):
        n2 = n1[i1 + 1:]
        for i2, t2 in enumerate(n2):
            for t3 in n2[i2 + 1:]:
                if t1 + t2 + t3 == s:
                    return t1, t2, t3

with open('input') as f:
    numbers = list(map(int, f.readlines()))

term1, term2, term3 = find_terms(numbers, 2020)
print(term1 * term2 * term3)
