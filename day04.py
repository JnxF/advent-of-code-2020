from aocd.models import Puzzle
import re

input: str = Puzzle(day=4, year=2020).input_data

fields = "byr iyr eyr hgt hcl ecl pid cid"
fields = set(fields.split(" "))


def part1():
    passports = input.split("\n\n")
    passports = [" ".join(t.split("\n")) for t in passports]
    passports = [t.split(" ") for t in passports]
    passports = [[w.split(":")[0] for w in t] for t in passports]
    validPassports = [t for t in passports if set(t + ["cid"]) == fields]
    return len(validPassports)


def part2():
    rules = [
        ("byr", lambda x: 1920 <= int(x) <= 2002),
        ("iyr", lambda x: 2010 <= int(x) <= 2020),
        ("eyr", lambda x: 2020 <= int(x) <= 2030),
        (
            "hgt",
            lambda x: len(x) > 2
            and (
                150 <= int(x[:-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[:-2]) <= 76
            ),
        ),
        (
            "hcl",
            lambda x: len(x) == 7
            and x[0] == "#"
            and all(c in "0123456789abcdef" for c in x[1:]),
        ),
        ("ecl", lambda x: x in "amb blu brn gry grn hzl oth"),
        ("pid", lambda x: len(x) == 9 and all("0" <= c <= "9" for c in x)),
    ]
    return sum(
        all(key in passport and f(passport[key]) for key, f in rules)
        for passport in (
            dict(map(lambda x: x.split(":"), part))
            for part in map(str.split, input.split("\n\n"))
        )
    )
