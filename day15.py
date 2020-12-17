from aocd.models import Puzzle
from math import ceil

input = [0, 3, 6]
final = []
d = dict()
i = 0
last = None
for idx, x in enumerate(input):
    d[x] = idx
    final.append(x)

for idx in range(len(input), 12):
    last = final[-1]
    if last in d.keys():
        res = idx - d[last] - 1
        d[last] = res + 1
    else:
        d[last] = idx
        res = 0
    final.append(res)
    print(i, ": ", res)

print(final)
