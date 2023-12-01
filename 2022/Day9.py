def move_head(h, dir):
    if dir == "R":
        h[0] += 1
    elif dir == "L":
        h[0] -= 1
    elif dir == "U":
        h[1] += 1
    else:
        h[1] -= 1

def move_tail(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        if h[1] != t[1]:
            t[1] += 1 if h[1] > t[1] else -1
        if h[0] != t[0]:
            t[0] += 1 if h[0] > t[0] else -1

# Part 1
with open("input.txt") as f:
    POS = set()
    POS.add((0, 0))
    h = [0, 0]
    t = [0, 0]
    for line in f:
        line = line.strip().split(" ")
        dir = line[0]
        n = int(line[1])
        for _ in range(n):
            move_head(h, dir)
            move_tail(h, t)
            POS.add((t[0], t[1]))
    print(POS)
    print(len(POS))

# Part 2
with open("input.txt") as f:
    POS = set()
    POS.add((0, 0))
    r = [[0, 0] for _ in range(10)]
    for line in f:
        line = line.strip().split(" ")
        dir = line[0]
        n = int(line[1])
        for _ in range(n):
            move_head(r[0], dir)
            for i in range(1, 10):
                move_tail(r[i-1], r[i])
            POS.add((r[9][0], r[9][1]))
    # print(POS)
    print(len(POS))