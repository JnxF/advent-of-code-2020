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
