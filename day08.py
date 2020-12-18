from aocd.models import Puzzle
from copy import deepcopy

input: str = Puzzle(day=8, year=2020).input_data
input = input.split("\n")
input = [instruction.split(" ") for instruction in input]
input = [(oper, int(arg)) for (oper, arg) in input]


def run(code):
    pc = 0
    visited = set()
    acc = 0
    while pc < len(code):
        if pc in visited:
            return (False, acc)
        visited.add(pc)
        oper, arg = code[pc]
        if oper == "acc":
            acc += arg
            pc += 1
        elif oper == "jmp":
            pc += arg
        elif oper == "nop":
            pc += 1
    return (True, acc)


def part1():
    _, accValue = run(input)
    return accValue


def part2():
    n = len(input)
    for i in range(n):
        modifiedInput = deepcopy(input)
        oper, arg = modifiedInput[i]
        if oper == "jmp":
            modifiedInput[i] = ("nop", arg)
        elif oper == "nop":
            modifiedInput[i] = ("jpm", arg)
        else:
            continue
        isSuccessful, accValue = run(modifiedInput)
        if isSuccessful:
            return accValue
