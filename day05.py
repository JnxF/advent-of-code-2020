from aocd.models import Puzzle

inputInBinary: str = (
    Puzzle(day=5, year=2020)
    .input_data.translate("".maketrans("FBLR", "0101"))
    .splitlines()
)

seatsIds = set(map(lambda code: int(code, 2), inputInBinary))


def part1():
    return max(seatsIds)


def part2():
    possibleIds = set(range(min(seatsIds), max(seatsIds) + 1))
    missingIds = possibleIds.difference(seatsIds)
    return list(missingIds)[0]
