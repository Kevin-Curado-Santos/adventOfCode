def part1(f):
    from collections import defaultdict
    data = f.read().splitlines()
    inst = [0 if c == 'L' else 1 for c in data[0]]
    
    elms = defaultdict(tuple)
    for l in data[2:]:
        l = l.split()
        elms[l[0]] = (l[2][1:-1], l[3].replace(')', ''))
    
    c = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        curr = elms[curr][inst[c%len(inst)]]
        c += 1
    print(c)



def part2(f):
    from collections import defaultdict
    import math
    data = f.read().splitlines()
    inst = [0 if c == 'L' else 1 for c in data[0]]
    
    elms = defaultdict(tuple)
    for l in data[2:]:
        l = l.split()
        elms[l[0]] = (l[2][1:-1], l[3].replace(')', ''))
    
    curr = [n for n in elms.keys() if n.endswith('A')]
    lc = []
    for n in curr:
        c = 0
        while not n.endswith('Z'):
            n = elms[n][inst[c%len(inst)]]
            c += 1
        lc.append(c)
        
    print(math.lcm(*lc))



if __name__ == '__main__':
    import sys

    with open('8.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
