from aocd.models import Puzzle
import math

input: str = Puzzle(day=3, year=2020).input_data.splitlines()
n = len(input)
m = len(input[0])


def part1():
    return [input[i][i * 3 % m] for i in range(n)].count("#")


def part2():
    def slope(input, right, down):
        howMany = (n - 1) // down + 1
        pos = [input[(i * down)][i * right % m] for i in range(howMany)]
        return pos.count("#")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    treesPerSlope = [slope(input, r, d) for (r, d) in slopes]
    return math.prod(treesPerSlope)
