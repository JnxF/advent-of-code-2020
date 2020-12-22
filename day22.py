from aocd.models import Puzzle
from math import prod

input: str = Puzzle(day=22, year=2020).input_data
player1, player2 = map(
    lambda player: list(map(int, player[1:])), map(str.splitlines, input.split("\n\n"))
)


def score(deck):
    return sum(map(prod, zip(deck, range(len(deck), 0, -1))))


def part1():
    p1 = player1.copy()
    p2 = player2.copy()
    while len(p1) > 0 and len(p2) > 0:
        t1 = p1.pop(0)
        t2 = p2.pop(0)
        if t1 > t2:
            p1 += [t1, t2]
        else:
            p2 += [t2, t1]
    return score(p1 if len(p2) == 0 else p2)


# (the first player wins, deck of the winning player)
def first_wins(p1, p2) -> tuple[bool, list[int]]:
    played_decks = set()
    while len(p1) > 0 and len(p2) > 0:
        if str((p1, p2)) in played_decks:
            return (True, p1)
        played_decks.add(str((p1, p2)))
        t1, t2 = p1.pop(0), p2.pop(0)
        first_wins_current = (
            first_wins(p1[:t1], p2[:t2])[0]
            if len(p1) >= t1 and len(p2) >= t2
            else (t1 > t2)
        )
        if first_wins_current:
            p1 += [t1, t2]
        else:
            p2 += [t2, t1]
    return (True, p1) if len(p2) == 0 else (False, p2)


def part2():
    _, winning_deck = first_wins(player1, player2)
    return score(winning_deck)
