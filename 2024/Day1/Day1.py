def parse():
    l1 = []
    l2 = []
    with open('day1.in') as f:
        for line in f:
            n, m = map(int, line.split())
            l1.append(n)
            l2.append(m)
    return l1, l2

def part1():
    ans = 0
    l1, l2 = parse()
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        ans += abs(l1[i] - l2[i])
    return ans

def part2helper(l1, l2):
    d = {}
    for i in l1:
        if i not in d:
            d[i] = i * l2.count(i)
    return d

def part2():
    ans = 0
    l1, l2 = parse()
    d = part2helper(l1, l2)
    for i in l1:
        ans += d[i]
    return ans

if __name__ == '__main__':
    print(part1())
    print(part2())