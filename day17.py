from aocd.models import Puzzle

input: str = Puzzle(day=17, year=2020).input_data
input = input.splitlines()
n = len(input)
m = len(input[0])
displacement = (n - 1) // 2
originalNodes = set()
for i in range(n):
    for j in range(m):
        if input[i][j] == "#":
            originalNodes.add((j - displacement, i - displacement, 0))


def active_neighbours(point, allThePoints):
    if len(point) == 3:
        x, y, z = point
        w = None
    else:
        x, y, z, w = point
    neighbours = []
    for X in [x - 1, x, x + 1]:
        for Y in [y - 1, y, y + 1]:
            for Z in [z - 1, z, z + 1]:
                if w is not None:
                    for W in [w - 1, w, w + 1]:
                        neighbours.append(((X, Y, Z, W), point))
                else:
                    neighbours.append(((X, Y, Z), point))
    return len(
        list(filter(lambda x: x[0] != x[1] and x[0] in allThePoints, neighbours))
    )


def iterate(current, fourdimensions=False):
    next = set()
    neighbours = []
    for point in current:
        if fourdimensions:
            x, y, z, w = point
        else:
            x, y, z = point
        if active_neighbours(point, current) in [2, 3]:
            next.add(point)
        for X in [x - 1, x, x + 1]:
            for Y in [y - 1, y, y + 1]:
                for Z in [z - 1, z, z + 1]:
                    if not fourdimensions:
                        neighbours.append(((X, Y, Z), point))
                    else:
                        for W in [w - 1, w, w + 1]:
                            neighbours.append(((X, Y, Z, W), point))
    neighbours = [
        point
        for (point, reference) in neighbours
        if active_neighbours(point, current) == 3
        and point != reference
        and point not in current
    ]
    next |= set(neighbours)
    return next


def part1():
    nodes = originalNodes.copy()
    for _ in range(6):
        nodes = iterate(nodes)
    return len(nodes)


def part2():
    nodes = set()
    for (x, y, z) in originalNodes:
        nodes.add((x, y, z, 0))
    for _ in range(6):
        nodes = iterate(nodes, fourdimensions=True)
    return len(nodes)
