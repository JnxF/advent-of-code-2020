from aocd.models import Puzzle
from aocd import submit

day = 1
year = 2020

input: str = Puzzle(year, day).input_data


def part1():
    lines = [int(x) for x in input.splitlines()]
    for (i, v1) in enumerate(lines):
        for (j, v2) in enumerate(lines):
            if i != j and v1 + v2 == 2020:
                submit(v1 * v2)
                exit()


def part2():
    lines = [int(x) for x in input.splitlines()]
    for (i, v1) in enumerate(lines):
        for (j, v2) in enumerate(lines):
            for (k, v3) in enumerate(lines):
                if i != j != k and v1 + v2 + v3 == 2020:
                    submit(v1 * v2 * v3)
                    exit()
