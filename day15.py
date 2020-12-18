from aocd.models import Puzzle

input = [9, 3, 1, 0, 8, 4]


def play(iterations):
    previous = dict()
    for idx, num in enumerate(input[:-1]):
        previous[num] = idx + 1
    last = input[-1]
    for i in range(len(input), iterations):
        if last in previous:
            next = i - previous[last]
        else:
            next = 0
        previous[last] = i
        last = next
    return last


def part1():
    return play(2020)


def part2():
    return play(30000000)
