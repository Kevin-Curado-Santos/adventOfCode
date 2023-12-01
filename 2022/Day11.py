from collections import defaultdict
from math import lcm, prod

ops = [
    lambda x: x*13,
    lambda x: x*x,
    lambda x: x+6,
    lambda x: x+2,
    lambda x: x+3,
    lambda x: x+4,
    lambda x: x+8,
    lambda x: x*7
]

test = [19, 7, 17, 13, 11, 2, 5, 3]
true = [5, 5, 1, 1, 3, 4, 4, 2]
false = [6, 0, 0, 2, 7, 6, 7, 3]

monkeys = [
    [72, 97],
    [55, 70, 90, 74, 95],
    [74, 97, 66, 57],
    [86, 54, 53],
    [50, 65, 78, 50, 62, 99],
    [90],
    [88, 92, 63, 94, 96, 82, 53, 53],
    [70, 60, 71, 69, 77, 70, 98]
]

# Part 1
i = 0
insp = defaultdict(int)
for _ in range(20 * len(monkeys)):
    items = monkeys[i]
    for item in items:
        insp[i] += 1
        new = ops[i](item)
        new //= 3
        if new % test[i] == 0:
            monkeys[true[i]].append(new)
        else:
            monkeys[false[i]].append(new)
    monkeys[i] = []
    i = (i + 1) % len(monkeys)
l = sorted(insp.values())[-2:]
print(prod(l))

# Part 2
i = 0
insp = defaultdict(int)
for _ in range(10000 * len(monkeys)):
    items = monkeys[i]
    for item in items:
        insp[i] += 1
        new = ops[i](item)
        new %= lcm(*test)
        if new % test[i] == 0:
            monkeys[true[i]].append(new)
        else:
            monkeys[false[i]].append(new)
    monkeys[i] = []
    i = (i + 1) % len(monkeys)

l = sorted(insp.values())[-2:]
print(prod(l))
