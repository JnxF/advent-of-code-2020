from aocd.models import Puzzle
from ast import parse, Constant, BinOp, Expression, Add

input: str = Puzzle(day=18, year=2020).input_data.splitlines()


def simpleEvaluator(exp):
    if type(exp) == str:
        exp = exp.replace("+", "PLUS").replace("*", "TIMES")
        exp = exp.replace("PLUS", "-").replace("TIMES", "+")
        return simpleEvaluator(parse(exp, mode="eval"))
    elif type(exp) == Constant:
        return exp.value
    elif type(exp) == Expression:
        return simpleEvaluator(exp.body)
    elif type(exp) == BinOp:
        left = simpleEvaluator(exp.left)
        right = simpleEvaluator(exp.right)
        return left * right if type(exp.op) == Add else left + right


def part1():
    return sum([simpleEvaluator(exp) for exp in input])


def advancedEvaluator(exp):
    exp = exp.replace("+", "PLUS").replace("*", "TIMES")
    exp = exp.replace("PLUS", "*").replace("TIMES", "+")
    return simpleEvaluator(parse(exp, mode="eval"))


def part2():
    return sum([advancedEvaluator(exp) for exp in input])
