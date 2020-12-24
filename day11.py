from aocd.models import Puzzle
from copy import deepcopy

input: str = Puzzle(day=11, year=2020).input_data
input = input.splitlines()
input = [list(line) for line in input]
n = len(input)
m = len(input[0])


def adjacent(i, j, state):
    ret = []
    for I in [i - 1, i, i + 1]:
        for J in [j - 1, j, j + 1]:
            if (i, j) != (I, J) and I >= 0 and J >= 0 and I < n and J < m:
                ret.append(state[I][J])
    return ret.count("#")


def iterate1(previousState):
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
        state = iterate1(state)
        currentSum = sum([line.count("#") for line in state])
        if currentSum == previousCount:
            return currentSum
        previousCount = currentSum


def adjacent2(i, j, state):
    total = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            (I, J) = (i + di, j + dj)
            while I >= 0 and J >= 0 and I < n and J < m and state[I][J] == ".":
                (I, J) = (I + di, J + dj)
            if I >= 0 and J >= 0 and I < n and J < m and state[I][J] == "#":
                total += 1

    return total


def iterate2(previousState):
    nextState = deepcopy(previousState)
    for i in range(n):
        for j in range(m):
            adjacentOccupiedCount = adjacent2(i, j, previousState)
            if previousState[i][j] == "L" and adjacentOccupiedCount == 0:
                nextState[i][j] = "#"
            elif previousState[i][j] == "#" and adjacentOccupiedCount >= 5:
                nextState[i][j] = "L"
    return nextState


def part2():
    state = deepcopy(input)
    previousCount = 0
    while True:
        state = iterate2(state)
        currentSum = sum([line.count("#") for line in state])
        if currentSum == previousCount:
            return currentSum
        previousCount = currentSum
