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
    def validate(p):
        try:
            keys = set(list(p.keys()) + ["cid"])
            if keys != fields:
                return False

            ok = True
            ok = (
                ok
                and len(p["byr"]) == 4
                and p["byr"].isdigit()
                and 1920 <= int(p["byr"]) <= 2002
            )
            ok = (
                ok
                and len(p["iyr"]) == 4
                and p["iyr"].isdigit()
                and 2010 <= int(p["iyr"]) <= 2020
            )
            ok = (
                ok
                and len(p["eyr"]) == 4
                and p["eyr"].isdigit()
                and 2020 <= int(p["eyr"]) <= 2030
            )
            hgtSplit = re.split("(\D+)", p["hgt"])
            hgtValue = int(hgtSplit[0])
            hgtUnit = hgtSplit[1]

            if hgtUnit == "cm":
                ok = ok and 150 <= hgtValue <= 193
            elif hgtUnit == "in":
                ok = ok and 59 <= hgtValue <= 76
            else:
                return False
            ok = ok and bool(re.match("#[0-9|a-f]{6}", p["hcl"]))
            ok = ok and p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            ok = ok and bool(re.match("[0-9]{9}", p["pid"]))
            return ok

        except:
            return False

    passports = input.split("\n\n")
    passports = [" ".join(t.split("\n")) for t in passports]
    passports = [t.split(" ") for t in passports]
    passports = [{w.split(":")[0]: w.split(":")[1] for w in t} for t in passports]
    passports = [p for p in passports if validate(p)]
    return len(passports)
