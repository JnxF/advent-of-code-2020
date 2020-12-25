from aocd.models import Puzzle

card, door = map(int, Puzzle(day=25, year=2020).input_data.splitlines())


def part1():
    res = 1
    card_loop_size = 0
    while True:
        res = (res * 7) % 20201227
        card_loop_size += 1
        if res == card:
            break
    encryption_key = 1
    for _ in range(card_loop_size):
        encryption_key = (encryption_key * door) % 20201227
    return encryption_key
