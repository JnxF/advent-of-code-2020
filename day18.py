from aocd.models import Puzzle
from collections import deque
from ast import parse, Constant, BinOp, Expression, Add

input: str = Puzzle(day=18, year=2020).input_data.splitlines()


def evaluate(exp):
    exp = exp.replace("(", " ( ").replace(")", " ) ")
    exp = exp.split(" ")
    exp = [i for i in exp if i != ""]

    stack = []
    while exp:
        if len(exp) > 0:
            top = exp[0]
            exp.pop(0)

            if top.isnumeric():
                top = int(top)
                stack.append(top)
            else:
                stack.append(top)

        while (
            len(stack) >= 3
            and type(stack[-1]) == int
            and type(stack[-2]) == str
            and type(stack[-3]) == int
        ):
            term2 = stack.pop()
            op = stack.pop()
            term1 = stack.pop()

            if op == "*":
                stack.append(term1 * term2)
            else:
                stack.append(term1 + term2)

        while (
            len(stack) >= 3
            and stack[-1] == ")"
            and type(stack[-2]) == int
            and stack[-3] == "("
        ):
            _ = stack.pop()
            res = stack.pop()
            _ = stack.pop()

            stack.append(res)

        while (
            len(stack) >= 3
            and type(stack[-1]) == int
            and type(stack[-2]) == str
            and type(stack[-3]) == int
        ):
            term2 = stack.pop()
            op = stack.pop()
            term1 = stack.pop()

            if op == "*":
                stack.append(term1 * term2)
            else:
                stack.append(term1 + term2)

        while (
            len(stack) >= 3
            and stack[-1] == ")"
            and type(stack[-2]) == int
            and stack[-3] == "("
        ):
            _ = stack.pop()
            res = stack.pop()
            _ = stack.pop()

            stack.append(res)

    return stack[0]


def part1():
    return sum([evaluate(e) for e in input])


def advancedEvaluator(exp):
    if type(exp) == str:
        exp = exp.replace("+", "PLUS").replace("*", "TIMES")
        exp = exp.replace("PLUS", "*").replace("TIMES", "+")
        return advancedEvaluator(parse(exp, mode="eval"))
    elif type(exp) == Constant:
        return exp.value
    elif type(exp) == Expression:
        return advancedEvaluator(exp.body)
    elif type(exp) == BinOp:
        left = advancedEvaluator(exp.left)
        right = advancedEvaluator(exp.right)
        return left * right if type(exp.op) == Add else left + right


def part2():
    return sum([advancedEvaluator(exp) for exp in input])
