from aocd.models import Puzzle

input: str = Puzzle(day=1, year=2020).input_data


def part1():
    lines = [int(x) for x in input.splitlines()]
    for (i, v1) in enumerate(lines):
        for (j, v2) in enumerate(lines):
            if i != j and v1 + v2 == 2020:
                return v1 * v2


def part2():
    lines = [int(x) for x in input.splitlines()]
    for (i, v1) in enumerate(lines):
        for (j, v2) in enumerate(lines):
            for (k, v3) in enumerate(lines):
                if i != j != k and v1 + v2 + v3 == 2020:
                    return v1 * v2 * v3
