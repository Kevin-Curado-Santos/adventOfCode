def shoelace(ps):
    n = len(ps)
    return abs(sum(ps[i][0]*ps[(i+1)%n][1] - ps[i][1]*ps[(i+1)%n][0] for i in range(n)))/2

def part1(f):
    data = f.read().splitlines()
    ans = 0
    coord = [(0, 0)]
    x, y = 0, 0
    for l in data:
        d, n, _ = l.split()
        if d == 'R':
            x += int(n)
        elif d == 'L':
            x -= int(n)
        elif d == 'U':
            y -= int(n)
        elif d == 'D':
            y += int(n)
        coord.append((x, y))    
    print(shoelace(coord))

def part2(f):
    data = f.read().splitlines()
    ans = 0
    print(ans)

if __name__ == '__main__':
    import sys

    with open('18test.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
