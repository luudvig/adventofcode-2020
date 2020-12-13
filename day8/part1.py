#!/usr/bin/env python3

from operator import add, sub

with open('input') as f:
    accumulator, executed, i, instructions = 0, set(), 0, f.read().splitlines()

while i not in executed:
    executed.add(i)
    instr, oper, term = instructions[i][:3], {'+': add, '-': sub}[instructions[i][4:5]], int(instructions[i][5:])

    i = oper(i, term) if instr == 'jmp' else i + 1
    accumulator = oper(accumulator, term) if instr == 'acc' else accumulator

print(accumulator)
