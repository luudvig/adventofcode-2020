#!/usr/bin/env python3

def recursive_combat(deck1, deck2):
    rounds = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in rounds:
            return deck1, []
        rounds.add((tuple(deck1), tuple(deck2)))
        c1, c2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= c1 and len(deck2) >= c2:
            subdeck1, subdeck2 = recursive_combat(deck1[:c1], deck2[:c2])
            deck1.extend([c1, c2]) if subdeck1 else deck2.extend([c2, c1])
        else:
            deck1.extend([c1, c2]) if c1 > c2 else deck2.extend([c2, c1])
    return deck1, deck2

with open('input') as f:
    players = f.read().split('\n\n')
    deck1 = [int(c) for c in players[0].splitlines()[1:]]
    deck2 = [int(c) for c in players[1].splitlines()[1:]]

deck1, deck2 = recursive_combat(deck1.copy(), deck2.copy())
score, winner = 0, reversed(deck1) if deck1 else reversed(deck2)

for i, c in enumerate(winner, 1):
    score = score + i * c

print(score)
