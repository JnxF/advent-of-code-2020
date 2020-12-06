from aocd.models import Puzzle

# from aocd import submit

input: str = Puzzle(day=6, year=2020).input_data.split("\n\n")


def part1():
    return sum([len(set(block.replace("\n", ""))) for block in input])


def joining(block):
    commonQuestions = block[0]
    for question in block[1:]:
        commonQuestions = commonQuestions.intersection(question)
    return len(commonQuestions)


def part2():
    groups = [[set(line) for line in block.split("\n")] for block in input]
    return sum([joining(block) for block in groups])
