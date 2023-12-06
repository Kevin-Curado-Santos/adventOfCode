def part1(f):
    ans = 0
    for l in f: 
        id, g = l.split(': ')
        for s in g.split('; '):
            c = [x.split() for x in s.split(', ')]
            ct = {b: int(a) for a, b in c}
            if not (ct.get('red', 0) <= 12 and ct.get('green', 0) <= 13 and ct.get('blue', 0) <= 14):
                break
        else:
            ans += int(id.split()[-1])
    print(ans)

def part2(f):
    ans = 0
    for l in f:
        id, g = l.split(': ')
        n = {'red': 0, 'green': 0, 'blue': 0}
        for s in g.split('; '):
            c = [x.split() for x in s.split(', ')]
            ct = {b: int(a) for a, b in c}
            n['red'] = max(n['red'], ct.get('red', 0))
            n['green'] = max(n['green'], ct.get('green', 0))
            n['blue'] = max(n['blue'], ct.get('blue', 0))
        ans += n['red'] * n['green'] * n['blue'] 
    print(ans)

if __name__ == '__main__':
    import sys
    with open('2.in') as f: 
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
