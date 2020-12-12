from aocd.models import Puzzle
from copy import deepcopy

input: str = Puzzle(day=12, year=2020).input_data
input = input.splitlines()
input = [(line[0], int(line[1:])) for line in input]


def part1():
    pos = complex(0, 0)
    dir = complex(1, 0)
    for (action, value) in input:
        if action == "N":
            pos += complex(0, value)
        if action == "S":
            pos += complex(0, -value)
        if action == "E":
            pos += complex(value, 0)
        if action == "W":
            pos += complex(-value, 0)
        if action == "L":
            dir *= complex(0, 1) ** (value // 90)
        if action == "R":
            dir *= complex(0, 1) ** (-value // 90)
        if action == "F":
            pos += value * dir
    return int(abs(pos.real) + abs(pos.imag))


def part2():
    pos = complex(0, 0)
    waypoint = complex(10, 1)
    for (action, value) in input:
        if action == "N":
            waypoint += complex(0, value)
        if action == "S":
            waypoint += complex(0, -value)
        if action == "E":
            waypoint += complex(value, 0)
        if action == "W":
            waypoint += complex(-value, 0)
        if action == "L":
            waypoint *= complex(0, 1) ** (value // 90)
        if action == "R":
            waypoint *= complex(0, 1) ** (-value // 90)
        if action == "F":
            pos += value * waypoint
    return int(abs(pos.real) + abs(pos.imag))
