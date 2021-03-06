from aocd.models import Puzzle

input: str = Puzzle(day=2, year=2020).input_data.splitlines()


def parseLine(line):
    lineSplitted = line.split(":")
    indexesAndLetter = lineSplitted[0].split(" ")
    password = lineSplitted[1].strip()
    letter = indexesAndLetter[1]
    indexes = indexesAndLetter[0].split("-")
    idx0 = int(indexes[0])
    idx1 = int(indexes[1])
    return (idx0, idx1, letter, password)


def part1():
    def validate1(line):
        (idx0, idx1, letter, password) = line
        return idx0 <= password.count(letter) <= idx1

    lines = [parseLine(line) for line in input]
    return len([line for line in lines if validate1(line)])


def part2():
    def validate2(line):
        (idx0, idx1, letter, password) = line
        p1 = password[idx0 - 1] == letter
        p2 = password[idx1 - 1] == letter
        # p1 xor p2
        return p1 != p2

    lines = [parseLine(line) for line in input]
    return len([line for line in lines if validate2(line)])
