from aocd.models import Puzzle
from ast import parse, Constant, BinOp, Expression, Add

input: str = Puzzle(day=18, year=2020).input_data.splitlines()


def reverseEvaluator(exp):
    if type(exp) == Constant:
        return exp.value
    elif type(exp) == Expression:
        return reverseEvaluator(exp.body)
    elif type(exp) == BinOp:
        left = reverseEvaluator(exp.left)
        right = reverseEvaluator(exp.right)
        return left * right if type(exp.op) == Add else left + right


def simpleEvaluator(exp):
    exp = exp.replace("+", "PLUS").replace("*", "TIMES")
    exp = exp.replace("PLUS", "-").replace("TIMES", "+")
    return reverseEvaluator(parse(exp, mode="eval"))


def part1():
    return sum([simpleEvaluator(exp) for exp in input])


def advancedEvaluator(exp):
    exp = exp.replace("+", "PLUS").replace("*", "TIMES")
    exp = exp.replace("PLUS", "*").replace("TIMES", "+")
    return reverseEvaluator(parse(exp, mode="eval"))


def part2():
    return sum([advancedEvaluator(exp) for exp in input])
