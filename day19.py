from aocd.models import Puzzle
import re

input: str = Puzzle(day=19, year=2020).input_data

rules, words = input.split("\n\n")


def map_line(line: str):
    rule_number, rule_content = line.split(": ")
    if "a" in rule_content:
        return (rule_number, "a")
    if "b" in rule_content:
        return (rule_number, "b")
    rule_content = rule_content.split(" | ")
    rule_content = [rc.split(" ") for rc in rule_content]
    return (rule_number, rule_content)


rules = [map_line(rule) for rule in rules.splitlines()]
rules = dict(rules)
words = words.splitlines()


def rule2regex(rule_number):
    rule_content = rules[rule_number]
    if type(rule_content) == str:
        return rule_content
    recursive_case = "|".join(
        ["".join([rule2regex(rule) for rule in option]) for option in rule_content]
    )
    return "(" + recursive_case + ")"


def part1():
    reg = "^" + rule2regex("0") + "$"
    return sum([bool(re.match(reg, word)) for word in words])


# 0 -> 42+ 42^n 31^n, with n >= 1
def testString2(s):
    r42 = "^" + rule2regex("42")
    r31 = "^" + rule2regex("31")

    howMany42 = 0
    howMany31 = 0
    while True:
        tryMatch = re.match(r42, s)
        if tryMatch is not None:
            idx = tryMatch.span()[1]
            s = s[idx:]
            howMany42 += 1
        else:
            break

    while True:
        tryMatch = re.match(r31, s)
        if tryMatch is not None:
            idx = tryMatch.span()[1]
            s = s[idx:]
            howMany31 += 1
        else:
            break

    return howMany31 >= 1 and howMany42 - howMany31 >= 1 and s == ""


def part2():
    return sum([testString2(word) for word in words])
