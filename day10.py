from aocd.models import Puzzle
from collections import defaultdict

input: str = Puzzle(day=10, year=2020).input_data
input = input.splitlines()
input = [int(line) for line in input]
bound = max(input)
input.sort()


def part1():
    d = defaultdict(lambda: 0)
    previous = 0
    d[3] += 1
    for c in input:
        d[c - previous] += 1
        previous = c
    return d[1] * d[3]


def part2():
    res = [1]
    for i in range(1, max(input) + 1):
        res.append(sum(res[-3:]) if i in input else 0)
    return res[-1]
