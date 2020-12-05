from aocd.models import Puzzle

# from aocd import submit

input: str = Puzzle(day=5, year=2020).input_data.splitlines()


def computeId(code):
    row = int(code[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(code[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column


seatsIds = set([computeId(seat) for seat in input])


def part1():
    return max(seatsIds)


def part2():
    possibleIds = set(range(min(seatsIds), max(seatsIds) + 1))
    missingIds = possibleIds.difference(seatsIds)
    return list(missingIds)[0]
