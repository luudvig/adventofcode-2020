#!/usr/bin/env python3

from functools import reduce

def solve_expr(expr):
    es = expr.split()
    for i in [i for i, e in enumerate(es) if e == '+']:
        es[i - 1], es[i], es[i + 1] = '1', '*', str(int(es[i - 1]) + int(es[i + 1]))
    return reduce(lambda f1, f2: f1 * f2, [int(n) for n in es if n != '*'])

with open('input') as f:
    expressions, sums = f.read().splitlines(), []

for expr in expressions:
    while expr.find('(') > -1:
        p1 = expr.rfind('(')
        p2 = expr.find(')', p1)
        expr = expr.replace(expr[p1:p2 + 1], str(solve_expr(expr[p1 + 1:p2])))
    sums.append(solve_expr(expr))

print(sum(sums))
