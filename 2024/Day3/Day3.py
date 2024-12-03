import re

def parse():
    l = [] 
    with open("day3.in", "r") as f:
        for line in f:
            s = re.findall("mul\(\d+,\d+\)", line)
            l.extend(s)
    return l

def parse2():
    l = []
    with open("day3.in", "r") as f:
        for line in f:
            r = '|'.join('(?:{0})'.format(x) for x in ("do\(\)", "don\'t\(\)", "mul\(\d+,\d+\)"))
            s = re.findall(r, line)
            l.extend(s) 
    return l
            

def part1():
    l = parse()
    ans = 0
    for s in l:
        a, b = map(int, s[4:-1].split(","))
        ans += a*b
    return ans

def part2():
    l = parse2()
    ans = 0
    ok = True
    for s in l:
        if s == "do()":
            ok = True
        elif s == "don't()":
            ok = False
        else:
            if ok:
                a, b = map(int, s[4:-1].split(","))
                ans += a*b
    return ans
    
    

if __name__ == "__main__":
    print(part1())
    print(part2())