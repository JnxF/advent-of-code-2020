from aocd.models import Puzzle

input: str = Puzzle(day=9, year=2020).input_data
input = input.splitlines()
input = [int(line) for line in input]

preamble = 25
n = len(input)


def part1():
    for idx in range(preamble, n):
        current = input[idx]
        currentPreamble = input[idx - preamble : idx]
        s = set(currentPreamble)
        isSumOfTwoPrevious = False
        for previous in currentPreamble:
            if (current - previous) in s and previous != current / 2:
                isSumOfTwoPrevious = True
                break
        if not isSumOfTwoPrevious:
            return current


def part2():
    invalidIndex = part1()
    carrySum = 0
    value2Idx = dict()
    for idx, current in enumerate(input):
        carrySum += current
        value2Idx[carrySum] = idx
        if carrySum - invalidIndex in value2Idx.keys():
            previousIndex = value2Idx[carrySum - invalidIndex] + 1
            contiguousSet = input[previousIndex : idx + 1]
            return min(contiguousSet) + max(contiguousSet)
