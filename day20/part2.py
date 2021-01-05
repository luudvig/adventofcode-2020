#!/usr/bin/env python3

from math import isqrt

def build_image(tiles, borders, x=0, y=0, m=set()):
    if y == isqrt(len(borders)):
        return tiles
    elif x + 1 == isqrt(len(borders)):
        nx, ny = 0, y + 1
    else:
        nx, ny = x + 1, y
    for i, t in borders.items():
        if i in m:
            continue
        m.add(i)
        for j, b in t.items():
            if x > 0 and borders[tiles[x - 1][y][0]][tiles[x - 1][y][1]][1] != b[3]:
                continue
            elif y > 0 and borders[tiles[x][y - 1][0]][tiles[x][y - 1][1]][2] != b[0]:
                continue
            tiles[x][y] = (i, j)
            result = build_image(tiles, borders, nx, ny, m)
            if result:
                return result
        m.remove(i)
    tiles[x][y] = None
    return None

def find_monsters(image):
    height, width, locations, pounds = 2, 19, set(), [
        (18, 0), (0, 1), (5, 1), (6, 1), (11, 1),
        (12, 1), (17, 1), (18, 1), (19, 1), (1, 2),
        (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)
    ]
    for y in range(len(image)):
        if y + height >= len(image):
            break
        for x in range(len(image[y])):
            if x + width >= len(image[y]):
                break
            found = True
            for ox, oy in pounds:
                if image[y + oy][x + ox] != '#':
                    found = False
                    break
            if found:
                for dx, dy in pounds:
                    locations.add((x + dx, y + dy))
    return locations

def get_image(tiles):
    options = {i: get_options(t) for i, t in tiles.items()}
    borders = {i: {j: get_borders(t) for j, t in enumerate(o)} for i, o in options.items()}
    dimension = isqrt(len(options))
    base = [[None] * dimension for i in range(dimension)]
    return build_image(base, borders), options

def get_borders(tile):
    return (tile[0], [l[-1] for l in tile], tile[-1], [l[0] for l in tile])

def get_flips(tile):
    return [tile, list(reversed(tile)), [list(reversed(l)) for l in tile], list(reversed([list(reversed(l)) for l in tile]))]

def get_options(tile):
    options, result = [], []
    for f in get_flips(tile):
        options.extend(get_rotations(f))
    for o in options:
        result.append(o) if o not in result else result
    return result

def get_rotations(tile):
    last, rotations = tile, [tile]
    for i in range(3):
        tile = [list(reversed(l)) for l in zip(*last)]
        last = tile
        rotations.append(tile)
    return rotations

def remove_borders(image, options):
    result = []
    for l in image:
        tiles = [[l[1:-1] for l in options[n][i][1:-1]] for n, i in l]
        for y in range(len(tiles[0][0])):
            line = []
            for i in range(len(tiles)):
                line.extend(tiles[i][x][y] for x in range(len(tiles[i])))
            result.append(line)
    return result

with open('input') as f:
    tiles = {int(p.partition('\n')[0][5:-1]): [[c for c in l] for l in p.splitlines()[1:]] for p in f.read().split('\n\n') if p}

image, options = get_image(tiles)
image = remove_borders(image, options)

for o in get_options(image):
    image, locations = o, find_monsters(o)
    if locations:
        break

filled = {(x, y) for y, l in enumerate(image) for x, c in enumerate(l) if c == '#'}
print(len(filled - locations))
