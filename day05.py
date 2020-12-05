from aocd.models import Puzzle
import math

# from aocd import submit

input: str = Puzzle(day=5, year=2020).input_data.splitlines()


def searchSpace(code, upper, lowerLetter, joiner):
    left = 0
    right = upper
    for c in code:
        if c == lowerLetter:
            right = math.floor((left + right) / 2)
        else:
            left = math.ceil((left + right) / 2)
    return joiner(left, right)


def computeId(code):
    row = searchSpace(code[:7], 127, "F", min)
    column = searchSpace(code[7:], 7, "L", max)
    return row * 8 + column


seatsIds = set([computeId(seat) for seat in input])


def part1():
    return max(seatsIds)


def part2():
    possibleIds = set(range(min(seatsIds), max(seatsIds) + 1))
    missingIds = possibleIds.difference(seatsIds)
    return list(missingIds)[0]
