from aocd.models import Puzzle
from collections import defaultdict
from re import findall

input: str = Puzzle(day=14, year=2020).input_data
input = input.splitlines()


def part1():
    mem = defaultdict(lambda x: 0)

    def applyMask(x):
        putZeros = int(mask.replace("X", "1"), 2)
        putOnes = int(mask.replace("X", "0"), 2)
        return x & putZeros | putOnes

    for line in input:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            address, value = findall(r"\d+", line)
            mem[int(address)] = applyMask(int(value))

    print(sum(mem.values()))


def iterate(s, idx):
    if idx >= len(s):
        return [s]
    if s[idx] == "X":
        res = []
        s = s[:idx] + "0" + s[idx + 1 :]
        res += iterate(s, idx + 1)
        s = s[:idx] + "1" + s[idx + 1 :]
        res += iterate(s, idx + 1)
        return res
    else:
        return iterate(s, idx + 1)


def part2():
    mem = defaultdict(lambda x: 0)

    def normalizeMask(m):
        m = m.replace("0", "U")
        res = iterate(m, 0)
        return [r.replace("U", "X") for r in res]

    def applyMask(x, ma):
        putZeros = int(ma.replace("X", "1"), 2)
        putOnes = int(ma.replace("X", "0"), 2)
        return x & putZeros | putOnes

    for line in input:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            address, value = findall(r"\d+", line)
            for submask in normalizeMask(mask):
                mem[applyMask(int(address), submask)] = int(value)
                print(applyMask(int(value), mask))

    print(sum(mem.values()))
