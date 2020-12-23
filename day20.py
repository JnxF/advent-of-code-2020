# This code is quite horrible
# Please don't look at it

from aocd.models import Puzzle
from copy import deepcopy
from math import prod, sqrt
from collections import defaultdict
import re

input: str = Puzzle(day=20, year=2020).input_data
if False:
    input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""
tiles = input.split("\n\n")
tiles = [[list(row) for row in tile.splitlines()] for tile in tiles]
tiles = {int(re.findall("\d+", "".join(tile[0]))[0]): tile[1:] for tile in tiles}
n = 10
num = int(sqrt(len(tiles)))


def dump(tile):
    for t in tile:
        print("".join([str(x) for x in t]))
    print()


def getColumns(tile):
    return list(zip(*tile))


def leftColumn(tile):
    return getColumns(tile)[0]


def rightColumn(tile):
    return getColumns(tile)[-1]


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


def trimedges(tile):
    t = deepcopy(tile)
    return [row[1:-1] for row in t[1:-1]]


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


def edges(t):
    return [
        "".join(topRow(t)),
        "".join(rightColumn(t)),
        "".join(bottomRow(t)),
        "".join(leftColumn(t)),
    ]


countAvailable = dict()
collisions = defaultdict(list)
for n1, tile in tiles.items():
    e1 = edges(tile)
    howMany = 0
    for n2, tile2 in tiles.items():
        if n1 == n2:
            continue
        e2 = edges(tile2)
        for e in e1:
            if e in e2 or e[::-1] in e2:
                howMany += 1
                collisions[n1] += e
    countAvailable[n1] = howMany

corners: list[int] = list(
    {k: v for k, v in sorted(countAvailable.items(), key=lambda item: item[1])}
)[:4]


def part1():
    return prod(corners)


# Take one of the corners and put it orientated
first = corners[0]
first_tile = tiles[first]
options = []

for ori in mutate(first_tile):
    for name, t in tiles.items():
        if first == name:
            continue
        for ori2 in mutate(t):
            if leftColumn(ori2) == rightColumn(ori):
                options.append(ori)

print(len(options))

result = [[] for _ in range(num)]
resultidx = [[] for _ in range(num)]
usedidx = set()
print("Fila INITIAL")

print("\t", "0")
# For the input, is 8
if num == 3:
    result[0].append(options[8])
else:
    result[0].append(options[2])
resultidx[0].append(first)

# Don't use any corner
for corner in corners:
    usedidx.add(corner)

# Find the first row

# Find one such that correctly oriented matches the previous
for j in range(num - 2):
    previous = result[0][-1]
    matchingColumn = rightColumn(previous)
    keepSearching = True
    for name, t in tiles.items():
        if not keepSearching:
            break
        if name in usedidx:
            continue
        for ori in mutate(t):
            if leftColumn(ori) == matchingColumn:
                keepSearching = False
                # Insertar
                print("\t", j + 1)
                result[0].append(ori)
                resultidx[0].append(name)
                usedidx.add(name)
                break

# Find a corner that fits
previous = result[0][-1]
matchingColumn = rightColumn(previous)
keepSearching = True
for name, t in tiles.items():
    if not keepSearching:
        break
    if name not in corners:
        continue
    for ori in mutate(t):
        if leftColumn(ori) == matchingColumn:
            keepSearching = False
            # Insertar
            print("\t", num - 1)
            result[0].append(ori)
            resultidx[0].append(name)
            usedidx.add(name)
            break

# add some that match with the top
for rowNumber in range(1, num - 1):
    print("Fila", rowNumber)
    for j in range(num):
        print("\t", j)
        goalRow = bottomRow(result[rowNumber - 1][j])
        for name, t in tiles.items():
            if name in usedidx:
                continue
            for ori in mutate(t):
                if topRow(ori) == goalRow:
                    result[rowNumber].append(ori)
                    resultidx[rowNumber].append(name)
                    usedidx.add(name)
                    break

# Last row
print("Fila LAST")
# First item
matchingRow = bottomRow(result[-2][0])
keepSearching = True
for name, t in tiles.items():
    if not keepSearching:
        break
    if name not in corners:
        continue
    for ori in mutate(t):
        if topRow(ori) == matchingRow:
            keepSearching = False
            # Insertar
            print("\t", 0)
            result[-1].append(ori)
            resultidx[-1].append(name)
            usedidx.add(name)
            break

# Rest of items
for j in range(1, num - 1):
    goalRow = bottomRow(result[-2][j])
    for name, t in tiles.items():
        if name in usedidx:
            continue
        for ori in mutate(t):
            if topRow(ori) == goalRow:
                print("\t", j)
                result[-1].append(ori)
                resultidx[-1].append(name)
                usedidx.add(name)
                break

# Last square
matchingColumn = rightColumn(result[-1][-1])
matchingRow = bottomRow(result[-2][-1])

keepSearching = True
for name, t in tiles.items():
    if not keepSearching:
        break
    if name not in corners:
        continue
    for ori in mutate(t):
        if leftColumn(ori) == matchingColumn and topRow(ori) == matchingRow:
            keepSearching = False
            # Insertar
            print("\t", num - 1)
            result[-1].append(ori)
            resultidx[-1].append(name)
            usedidx.add(name)
            break


# Trim edges from each square
result = [list(map(trimedges, row)) for row in result]

result2 = []
for megaRow in range(num):
    for i in range(n - 2):
        fila = ""
        for j in range(num):
            fila += "".join("".join(result[megaRow][j][i]))
        result2.append(list(fila))

monster = [[], [], []]
monster[0] = list("                  # ")
monster[1] = list("#    ##    ##    ###")
monster[2] = list(" #  #  #  #  #  #   ")

ymons = len(monster)
xmons = len(monster[0])


def larotacion(r):
    def Transposed(tile):
        return list("".join(row) for row in zip(*tile))

    def Reversed_tile(tile):
        return ["".join(reversed(row)) for row in tile]

    def Rotations(tile):
        ans = [tile]
        for _ in range(3):
            ans.append(Reversed_tile(Transposed(ans[-1])))
        return ans

    def Group(tile):
        return Rotations(tile) + Rotations(Transposed(tile))

    return Group(r)


for ori in larotacion(result2):
    ori = [list(n) for n in ori]
    howMany = 0
    for i in range(len(ori) - ymons + 1):
        for j in range(len(ori[0]) - xmons + 1):
            locations = []
            for mi in range(len(monster)):
                for mj in range(len(monster[0])):
                    if monster[mi][mj] == " ":
                        continue
                    if ori[i + mi][j + mj] != ".":
                        locations.append((i + mi, j + mj))
            if len(locations) >= 15:
                howMany += 1
                for a, b in locations:
                    ori[a][b] = "O"

    print(howMany, sum(["".join(row).count("#") for row in ori]))
