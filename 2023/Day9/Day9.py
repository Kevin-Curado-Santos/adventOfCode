def seq(ns, part2=False):
    l = []
    for i in range(len(ns)-1):
        l.append(ns[i+1]-ns[i])
    if all(x==0 for x in l):
        return ns[0 if part2 else -1]
    else:
        return ns[0 if part2 else -1] + (-1 if part2 else 1)*seq(l, part2)

def part1(f):
    data = f.read().splitlines()
    ans = 0
    for l in data:
        ns = [int(x) for x in l.split()]
        ans += seq(ns)
    print(ans)

def part2(f):
    data = f.read().splitlines()
    ans = 0
    for l in data:
        ns = [int(x) for x in l.split()]
        ans += seq(ns, True)
    print(ans)

if __name__ == '__main__':
    import sys

    with open('9.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)