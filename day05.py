from aocd.models import Puzzle

# from aocd import submit

input: str = Puzzle(day=5, year=2020).input_data.splitlines()


def computeId(code):
    binaryCode = code.replace("F", "0").replace("B", "1")
    binaryCode = binaryCode.replace("L", "0").replace("R", "1")
    return int(binaryCode, 2)


seatsIds = set(map(computeId, input))


def part1():
    return max(seatsIds)


def part2():
    possibleIds = set(range(min(seatsIds), max(seatsIds) + 1))
    missingIds = possibleIds.difference(seatsIds)
    return list(missingIds)[0]
