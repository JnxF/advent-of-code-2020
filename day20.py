from aocd.models import Puzzle
from copy import deepcopy
from json import dumps
import re

input: str = Puzzle(day=20, year=2020).input_data

tiles = input.split("\n\n")
tiles = [[list(row) for row in tile.splitlines()] for tile in tiles]
tiles = {int(re.findall("\d+", "".join(tile[0]))[0]): tile[1:] for tile in tiles}
n = 10


def getColumns(tile):
    return list(zip(*tile))


def leftColumn(tile):
    return getColumns(tile)[0]


def rightColumn(tile):
    return getColumns(tile)[0]


def topRow(tile):
    return tile[0]


def bottomRow(tile):
    return tile[-1]


def flipX(tile):
    t = deepcopy(tile)
    for i in range(n):
        for j in range(n):
            t[i][j] = tile[i][n - 1 - j]
    return t


def flipY(tile):
    t = deepcopy(tile)
    return t[::-1]


def transpose(tile):
    t = deepcopy(tile)
    for i in range(n):
        for j in range(n):
            t[i][j] = tile[j][i]
    return t


def rotate(tile):
    t = deepcopy(tile)
    return [row[::-1] for row in transpose(t)]


def mutate(tile):
    return [
        # Nothing
        tile,
        rotate(tile),
        rotate(rotate(tile)),
        rotate(rotate(rotate(tile))),
        # X
        flipX(tile),
        flipX(rotate(tile)),
        flipX(rotate(rotate(tile))),
        flipX(rotate(rotate(rotate(tile)))),
        # Y
        flipY(tile),
        flipY(rotate(tile)),
        flipY(rotate(rotate(tile))),
        flipY(rotate(rotate(rotate(tile)))),
        # X and Y
        flipX(flipY(tile)),
        flipX(flipY(rotate(tile))),
        flipX(flipY(rotate(rotate(tile)))),
        flipX(flipY(rotate(rotate(rotate(tile))))),
    ]


mutations = dict()
for k, v in tiles.items():
    mutations[k] = mutate(v)


def getSides(tile):
    l = [topRow(tile), rightColumn(tile), bottomRow(tile), leftColumn(tile)]
    l += [a[::-1] for a in l]
    l = ["".join(a) for a in l]
    return set(l)


def part1():
    # 2161*2753*2927*1201
    # Upper top left tile is one such that
    # 1) the TOP ROW doesn't match with any BOTTOM ROW
    # 2) the FIRST COLUMN doesn't match with any LAST COLUMN
    for tileName1, tile1 in tiles.items():
        total = 0
        for tileName2, tile2 in tiles.items():
            for tileName3, tile3 in tiles.items():
                if tileName2 >= tileName3:
                    continue
                if len(set([tileName1, tileName2, tileName3])) != 3:
                    continue

                options1 = mutations[tileName1]
                options2 = mutations[tileName2]
                options3 = mutations[tileName3]

                # if len(getSides(tile1).intersection(getSides(tile2))) == 0 and len(getSides(tile1).intersection(getSides(tile3))) == 0:
                #    continue

                for o1 in options1:
                    for o2 in options2:
                        for o3 in options3:
                            if topRow(o1) == bottomRow(o2) and leftColumn(
                                o1
                            ) == rightColumn(o3):
                                total += 1

                                # print(tileName1, tileName2, tileName3)
                                # print("o1", dumps([''.join(r) for r in o1], indent=4))
                                # print("o2", dumps([''.join(r) for r in o2], indent=4))
                                # print("o3", dumps([''.join(r) for r in o3], indent=4))
        print(tileName1, total)


corners = [2161, 2753, 2927, 1201]

# Put 2161 in the left corner
# accordingly so that it matches with something

# Check all orientations...
# for o1 in mutations[2161]:
#     total = 0
#     # So that given a top and left ones, are impossible to find them
#     for tileName2, tile2 in tiles.items():
#         for tileName3, tile3 in tiles.items():
#             if len(set([2161, tileName2, tileName3])) != 3:
#                 continue

#             options2 = mutations[tileName2]
#             options3 = mutations[tileName3]

#             for o2 in options2:
#                 for o3 in options3:
#                     if topRow(o1) == bottomRow(o2) and leftColumn(o1) == rightColumn(o3):
#                         total += 1
#     print(total)

# Find one such that the left matches with the right of the previous

solution = [[] for _ in range(12)]
solutionidx = [[] for _ in range(12)]
used = set()

solution[0].append(flipX(flipY(tiles[2161])))
solutionidx[0].append(2161)
used.add(2161)

while True:
    found = False
    previous = solution[0][-1]
    print(solutionidx[0][-1])
    for tileName, tileValue in tiles.items():
        if found:
            break
        if tileName in used:
            continue
        mu = mutations[tileName]
        for m in mu:
            if rightColumn(previous) == leftColumn(m):
                solution[0].append(m)
                solutionidx[0].append(tileName)
                used.add(tileName)
                found = True
                break
    print(solutionidx[0])
