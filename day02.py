from aocd.models import Puzzle

# from aocd import submit

input: str = Puzzle(day=2, year=2020).input_data.splitlines()


def prettyLine(line):
    s = line.split(":")
    numLet = s[0].split(" ")
    let = numLet[1]
    nums = numLet[0].split("-")
    n0 = int(nums[0])
    n1 = int(nums[1])
    return (n0, n1, let, s[1].strip())


def part1():
    def validate1(line):
        (n0, n1, let, s) = line
        return n0 <= s.count(let) <= n1

    lines = [prettyLine(line) for line in input]
    return len(list(filter(validate1, lines)))


def part2():
    def validate2(line):
        (n0, n1, let, s) = line
        n0 -= 1
        n1 -= 1
        p1 = s[n0] == let
        p2 = s[n1] == let
        return p1 != p2

    lines = [prettyLine(line) for line in input]
    return len(list(filter(validate2, lines)))
