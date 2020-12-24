from aocd.models import Puzzle

input: str = Puzzle(day=24, year=2020).input_data.splitlines()

directions = {
    "e": (1 + 0j),
    "nw": (0 + 1j),
    "se": (0 - 1j),
    "sw": (-1 - 1j),
    "w": (-1 + 0j),
    "ne": (1 + 1j),
}

blacks = set()
for line in input:
    res = []
    while line != "":
        for dir in directions.keys():
            if line.startswith(dir):
                line = line[len(dir) :]
                res.append(dir)
    p = 0 + 0j
    for e in res:
        p += directions[e]
    if p not in blacks:
        blacks.add(p)
    else:
        blacks.remove(p)


def part1():
    return len(blacks)


def surroundings(tile):
    return [tile + dir for dir in directions.values()]


def num_surrounding_blacks(tile, s):
    return len([surr for surr in surroundings(tile) if surr in s])


def part2():
    global blacks
    for _ in range(100):
        newblacks = set()
        # Any black tile with zero or more than 2 black tiles immediately
        # adjacent to it is flipped to white.
        for tile in blacks:
            if num_surrounding_blacks(tile, blacks) in [1, 2]:
                newblacks.add(tile)
        # Any white tile with exactly 2 black tiles immediately
        # adjacent to it is flipped to black.
        for tile in blacks:
            for adj in surroundings(tile):
                if adj not in blacks and num_surrounding_blacks(adj, blacks) == 2:
                    newblacks.add(adj)
        blacks = newblacks
    return len(blacks)
