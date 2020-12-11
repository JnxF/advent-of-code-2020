from aocd.models import Puzzle
from copy import deepcopy

input: str = Puzzle(day=11, year=2020).input_data
input = input.splitlines()
input = [list(line) for line in input]
n = len(input)
m = len(input[0])


def ok(i, j):
    return i >= 0 and j >= 0 and i < n and j < m


def adjacent(i, j, state):
    ret = []
    if ok(i - 1, j + 1):
        ret.append(state[i - 1][j + 1])
    if ok(i - 1, j + 0):
        ret.append(state[i - 1][j + 0])
    if ok(i - 1, j - 1):
        ret.append(state[i - 1][j - 1])
    if ok(i, j + 1):
        ret.append(state[i][j + 1])
    if ok(i, j - 1):
        ret.append(state[i][j - 1])
    if ok(i + 1, j + 1):
        ret.append(state[i + 1][j + 1])
    if ok(i + 1, j + 0):
        ret.append(state[i + 1][j + 0])
    if ok(i + 1, j - 1):
        ret.append(state[i + 1][j - 1])
    return ret.count("#")


def iterate(previousState):
    nextState = deepcopy(previousState)
    for i in range(n):
        for j in range(m):
            adjacentOccupiedCount = adjacent(i, j, previousState)
            if previousState[i][j] == "L" and adjacentOccupiedCount == 0:
                nextState[i][j] = "#"
            elif previousState[i][j] == "#" and adjacentOccupiedCount >= 4:
                nextState[i][j] = "L"
    return nextState


def part1():
    state = deepcopy(input)
    previousCount = 0

    while True:
        state = iterate(state)
        currentSum = sum([line.count("#") for line in state])
        if currentSum == previousCount:
            return currentSum
        previousCount = currentSum


def part2():
    pass
