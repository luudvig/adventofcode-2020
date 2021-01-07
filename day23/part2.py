#!/usr/bin/env python3

def crab(cups, pad=1000000):
    circ, head, m = [i + 1 for i in range(pad + 1)], cups[0], 0

    for i, l in enumerate(cups[:-1]):
        circ[l] = cups[i + 1]

    if pad > len(cups):
        circ[-1] = head
        circ[cups[-1]] = max(cups) + 1
    else:
        circ[cups[-1]] = head

    while m < 10000000:
        m, rem = m + 1, circ[head]
        circ[head] = circ[circ[circ[rem]]]
        allr = rem, circ[rem], circ[circ[rem]]
        dest = head - 1 if head > 1 else pad

        while dest in allr:
            dest = dest - 1 if dest != 1 else pad

        circ[circ[circ[rem]]] = circ[dest]
        circ[dest] = rem
        head = circ[head]

    cup = circ[1]
    while cup != 1:
        yield cup
        cup = circ[cup]

with open('input') as f:
    cups = [int(l) for l in f.readline().strip()]

result = crab(cups)
print(next(result) * next(result))
