from collections import defaultdict

def parse():
    with open("idk.in", "r") as f:
        r, u = f.read().split("\n\n")
    r = [tuple(map(int, x.split("|"))) for x in r.split("\n")]
    u = [list(map(int, x.split(","))) for x in u.split("\n")]
    return r, u

def part1():
    r, u = parse()

    c = []
    for x in u:
        ok = True
        d = {a: i for i, a in enumerate(x)}
        for a, b in r:
            if a in d and b in d and d[a] > d[b]:
                ok = False
                break
        if ok:
            c.append(x)
                
    return sum(x[len(x)//2] for x in c)

def part2():
    r, u = parse()
    
    c = []
    for x in u:
        d = {a: i for i, a in enumerate(x)}
        for a, b in r:
            if a in d and b in d and d[a] > d[b]:
                c.append(x)
                break
            
    g = defaultdict(list)
    for x in r:
        g[x[0]].append(x[1])

    for x in c:
        ok = True
        while ok:
            ok = False
            for i in range(len(x)-1):
                a, b = x[i], x[i+1]
                if a in g and b in g[a]:
                    x[i], x[i+1] = x[i+1], x[i]
                    ok = True
    
    return sum(x[len(x)//2] for x in c)
        

if __name__ == "__main__":
    print(part1())
    print(part2())