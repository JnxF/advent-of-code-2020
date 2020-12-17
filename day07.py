from aocd.models import Puzzle
from re import match

input: str = Puzzle(day=7, year=2020).input_data


def nextProcesser(s):
    if s == "no other bags":
        return []
    s = [tuple(match(r"\s*(\d+) (\w+ \w+)", a).groups()) for a in s.split(",")]
    return s


input = input.splitlines()
regex = r"^(\w+ \w+) bags contain (.+)\.$"
input = [list(match(regex, line).groups()) for line in input]
input = [(name, nextProcesser(inside)) for (name, inside) in input]
input = dict(input)


def part1():
    upperBags = set(["shiny gold"])
    previousSize = 0
    while len(upperBags) != previousSize:
        for (bagName, bags) in input.items():
            for (_, bagSubname) in bags:
                if bagSubname in upperBags:
                    upperBags.add(bagName)
        previousSize = len(upperBags)
    return previousSize - 1


def countBags(bagName):
    if len(input[bagName]) == 0:
        return 1
    total = 0
    for (bagCount, subBag) in input[bagName]:
        total += int(bagCount) * (countBags(subBag))
    return total + 1


def part2():
    return countBags("shiny gold") - 1
