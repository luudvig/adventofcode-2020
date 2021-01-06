#!/usr/bin/env python3

with open('input') as f:
    players = f.read().split('\n\n')
    deck1 = [int(c) for c in players[0].splitlines()[1:]]
    deck2 = [int(c) for c in players[1].splitlines()[1:]]

while deck1 and deck2:
    c1, c2 = deck1.pop(0), deck2.pop(0)
    deck1.extend([c1, c2]) if c1 > c2 else deck2.extend([c2, c1])

score, winner = 0, reversed(deck1) if deck1 else reversed(deck2)
for i, c in enumerate(winner, 1):
    score = score + i * c

print(score)
