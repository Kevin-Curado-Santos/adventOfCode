def parse():
    l = []
    with open("day2.in", "r") as f:
        for line in f:
            l.append(list(map(int, line.split())))
    return l

def part1():
    l = parse()
    ans = 0
    for e in l:
        diff = [b-a for a, b in zip(e, e[1:])]
        if (max(diff) < 0 and min(diff) >= -3) or (min(diff) > 0 and max(diff) <= 3):
            ans += 1
            
    return ans

def part2():
    l = parse()
    ans = 0
    for e in l:
        for i in range(len(e)):
            e2 = e[:i] + e[i+1:]
            diff = [b-a for a, b in zip(e2, e2[1:])]
            if (max(diff) < 0 and min(diff) >= -3) or (min(diff) > 0 and max(diff) <= 3):
                ans += 1
                break
            
    return ans

if __name__ == "__main__":
    print(part1())
    print(part2())