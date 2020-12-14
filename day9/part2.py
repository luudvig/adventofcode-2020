#!/usr/bin/env python3

def find_terms(l, c, s):
    for i, n in enumerate(l[c:], c):
        if sum(l[i - c:i]) == s:
            return l[i - c:i]
    return []

def validate(l, s):
    for i, t1 in enumerate(l):
        for t2 in l[i + 1:]:
            if t1 + t2 == s:
                return True
    return False

with open('input') as f:
    c, i, numbers, terms = 2, 25, list(map(int, f.readlines())), []

while validate(numbers[i - 25:i], numbers[i]):
    i = i + 1

while not terms:
    terms = sorted(find_terms(numbers, c, numbers[i]))
    c = c + 1

print(terms[0] + terms[-1])
