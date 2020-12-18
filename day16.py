from aocd.models import Puzzle
from copy import deepcopy
import re

input: str = Puzzle(day=16, year=2020).input_data

tags, yourticket, tickets = input.split("\n\n")
regex = r"(?P<tag>[^:]+): (?P<l1>\d+)-(?P<l2>\d+) or (?P<l3>\d+)-(?P<l4>\d+)"
tags = tags.splitlines()
tags = [re.match(regex, x).groups() for x in tags]
tags = [(tag, int(l1), int(l2), int(l3), int(l4)) for (tag, l1, l2, l3, l4) in tags]
yourticket = [int(x) for x in yourticket.splitlines()[1].split(",")]
tickets = tickets.splitlines()[1:]
tickets = [[int(t) for t in line.split(",")] for line in tickets]


def containsValid(tag, currentValue):
    _, l1, l2, l3, l4 = tag
    return l1 <= currentValue <= l2 or l3 <= currentValue <= l4


scanningRate = 0
validTickets = []
for ticket in tickets:
    isTicketOkay = True
    for item_ticket in ticket:
        ok = False
        for t in tags:
            if containsValid(t, item_ticket):
                ok = True
        if not ok:
            scanningRate += item_ticket
            isTicketOkay = False
            break
    if isTicketOkay:
        validTickets.append(ticket)

validTickets.append(yourticket)


def part1():
    return scanningRate


def part2():
    d = dict()
    zipped = list(zip(*validTickets))
    for idx, row in enumerate(zipped):
        row = list(row)
        validTags = deepcopy(tags)
        for currentValue in row:
            validTags = [vt for vt in validTags if containsValid(vt, currentValue)]
        d[idx] = validTags

    idx2tag = dict()
    ticketSize = len(yourticket)
    for _ in range(ticketSize):
        searchedTag = None
        for k, v in d.items():
            if len(v) == 1:
                searchedTag = v[0]
                idx2tag[k] = searchedTag[0]
                break

        for k in d.keys():
            if searchedTag in d[k]:
                d[k].remove(searchedTag)

    mul = 1
    for idx, tag in idx2tag.items():
        if tag.startswith("departure"):
            mul *= yourticket[idx]

    return mul
