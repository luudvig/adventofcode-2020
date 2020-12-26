#!/usr/bin/env python3

from operator import add, mul

def solve_expr(expr):
    ans, es = int(expr.split()[0]), expr.split()[1:]
    for i in [i for i, e in enumerate(es) if e == '+' or e == '*']:
        ans = {'+': add, '*': mul}[es[i]](ans, int(es[i + 1]))
    return ans

with open('input') as f:
    expressions, sums = f.read().splitlines(), []

for expr in expressions:
    while expr.find('(') > -1:
        p1 = expr.rfind('(')
        p2 = expr.find(')', p1)
        expr = expr.replace(expr[p1:p2 + 1], str(solve_expr(expr[p1 + 1:p2])))
    sums.append(solve_expr(expr))

print(sum(sums))
