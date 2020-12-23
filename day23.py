from aocd.models import Puzzle

input: str = Puzzle(day=23, year=2020).input_data
input = [int(n) for n in list(input)]


def part1():
    cups = input.copy()
    n = len(cups)
    i = 0
    for move in range(100):
        current = cups[i]
        pickup = (cups + cups)[i + 1 : i + 4]
        # print("-- move", move+1, " --")
        # print("cups:", ''.join(" " + str(t) + " " if i != idx else "(" + str(t) + ")" for (idx,t) in enumerate(cups)))
        # print("pick up:", ', '.join([str(p) for p in pickup]))
        next = cups[(i + 4) % n]
        for p in pickup:
            cups.remove(p)
        destination = current - 1
        while destination not in cups:
            destination -= 1
            if destination < min(cups):
                destination = max(cups)
        # print("destination:", destination)
        # print()
        idx = cups.index(destination)
        cups = cups[: idx + 1] + pickup + cups[idx + 1 :]
        i = cups.index(next)
    t = cups.index(1)
    return int("".join([str(num) for num in cups[t + 1 :] + cups[:t]]))


def part2():
    cups = input.copy()
    previous = max(cups) + 1
    while len(cups) != 1000000:
        cups.append(previous)
        previous += 1
    pointer = dict()
    previous = cups[-1]
    for v in cups:
        pointer[previous] = v
        previous = v
    mymax = max(cups)
    mymin = min(cups)
    current = cups[0]
    for _ in range(10000000):
        pickup_head = pointer[current]
        pickup_mid = pointer[pickup_head]
        pickup_end = pointer[pickup_mid]
        pickup = [pickup_head, pickup_mid, pickup_end]
        meganext = pointer[pickup_end]
        next = current - 1
        while next in pickup or next < mymin:
            next -= 1
            if next < mymin:
                next = mymax
        nextOfNext = pointer[next]
        pointer[current] = meganext
        pointer[next] = pickup_head
        pointer[pickup_end] = nextOfNext
        current = pointer[current]
    return pointer[1] * pointer[pointer[1]]
