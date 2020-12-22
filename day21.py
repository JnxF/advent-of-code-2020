from collections import Counter
from aocd.models import Puzzle

input: str = Puzzle(day=21, year=2020).input_data

ingredient_counter = Counter()
alergen2ingredients = {}

for food in input.splitlines():
    ingredients, alergens = food.split(" (contains ")
    ingredients = ingredients.split()
    alergens = alergens[:-1].split(", ")

    ingredient_counter.update(ingredients)

    for alergen in alergens:
        if alergen in alergen2ingredients:
            alergen2ingredients[alergen] &= set(ingredients)
        else:
            alergen2ingredients[alergen] = set(ingredients)

singles = set()
while len(singles) != len(alergen2ingredients):
    for alg, ings in alergen2ingredients.items():
        if len(ings) == 1:
            singles |= ings
        else:
            ings -= singles


def part1():
    return sum(
        count
        for ingredient, count in ingredient_counter.items()
        if ingredient not in set.union(*alergen2ingredients.values())
    )


def part2():
    return ",".join(
        alergen2ingredients[alergen].pop() for alergen in sorted(alergen2ingredients)
    )
