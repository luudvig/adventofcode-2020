#!/usr/bin/env python3

from operator import add, sub

with open('input') as f:
    accumulator, changed, executed, i, instructions, switch = 0, set(), set(), 0, f.read().splitlines(), True

while i < len(instructions):
    executed.add(i)
    instr, oper, term = instructions[i][:3], {'+': add, '-': sub}[instructions[i][4:5]], int(instructions[i][5:])

    if switch and instr != 'acc' and i not in changed:
        switch, instr = False, 'jmp' if instr == 'nop' else 'nop'
        changed.add(i)

    i = oper(i, term) if instr == 'jmp' else i + 1
    accumulator = oper(accumulator, term) if instr == 'acc' else accumulator

    if i in executed:
        accumulator, executed, i, switch = 0, set(), 0, True

print(accumulator)
