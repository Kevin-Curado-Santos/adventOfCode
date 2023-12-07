from collections import Counter

def score(cards):
    l = [b for _, b in Counter(cards).most_common()]
    if 5 in l:
        return 1
    elif 4 in l:
        return 2
    elif 3 in l and 2 in l:
        return 3
    elif 3 in l:
        return 4
    elif l.count(2) == 2:
        return 5
    elif l.count(2) == 1:
        return 6
    else:
        return 7

def part1(f):
    o = "AKQJT98765432"
    v = []
    for l in f:
        c, b = l.split()
        v.append((score(c), [o.index(x) for x in c] ,int(b)))
    v.sort(reverse=True)
    print(sum((i + 1) * x[-1] for i, x in enumerate(v)))
      
def part2(f):
    from itertools import product
    o = "AKQT98765432J"
    v = []
    for l in f:
        c, b = l.split()
        s = score(c)
        for st in product(o[:-1], repeat=c.count("J")):
            s = min(s, score(c.replace("J", "") + "".join(st)))
                
        v.append((s, [o.index(x) for x in c] ,int(b)))
    v.sort(reverse=True)
    print(sum((i + 1) * x[-1] for i, x in enumerate(v)))
        
  


if __name__ == '__main__':
    import sys

    with open('7.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
