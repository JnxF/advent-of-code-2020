from aocd.models import Puzzle
from math import ceil

input: str = Puzzle(day=13, year=2020).input_data.splitlines()
time = int(input[0])
times = [int(x) for x in input[1].split(",") if x != "x"]


def part1():
    times2 = [ceil(time / t) * t for t in times]
    zipped = zip(times, times2)
    a, b = min(zipped, key=lambda x: x[1])
    return a * (b - time)
