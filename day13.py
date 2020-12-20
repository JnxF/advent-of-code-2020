from aocd.models import Puzzle
from functools import reduce
from math import ceil

timeline, timesline = Puzzle(day=13, year=2020).input_data.splitlines()
timestamp = int(timeline)
timesline = timesline.split(",")


def part1():
    times = [int(x) for x in timesline if x != "x"]
    times2 = [ceil(timestamp / t) * t for t in times]
    zipped = zip(times, times2)
    a, b = min(zipped, key=lambda x: x[1])
    return a * (b - timestamp)


def part2():
    times_paired = enumerate(timesline)
    times_paired = [
        (int(id) - offset, int(id)) for (offset, id) in times_paired if id != "x"
    ]
    departures, ids = list(zip(*times_paired))
    # ∀ id ∈ ids . ∀ departure ∈ departures . x === departure (mod id)
    return chinese_remainder(ids, departures)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1
