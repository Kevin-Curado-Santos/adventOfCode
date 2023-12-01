from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sizes = defaultdict(int)
stack = []
for line in lines:
    if line.startswith("$ cd "):
        x = line[5:]
        if x == "/":
            stack = []
        elif x == "..":
            stack.pop()
        else:
            stack.append(x)
    elif line[0] != "$":
        a, _ = line.split()
        if a != "dir":
            for i in range(len(stack) + 1):
                path = "/" + "/".join(stack[:i])
                sizes[path] += int(a)


print(sizes)
# # Part 1
# print(sum([x for x in sizes.values() if x <= 100000]))

# # Part 2
# unused = 70000000 - sizes["/"]
# need = 30000000 - unused
# print(min([x for x in sizes.values() if x >= need]))