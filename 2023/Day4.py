def part1(f):
    ans=0
    for l in f:
        _, cs = l.split(': ')
        c1, c2 = cs.split('|')
        c1 = [int(x) for x in c1.split()]
        c2 = [int(x) for x in c2.split()]
        c = len(set(c1) & set(c2))
        if c>0:
            ans+=2**(c-1)
    print(ans)

def part2(f):
    from collections import defaultdict
    d = defaultdict(int)
    for i,l in enumerate(f):
        d[i] += 1
        _, cs = l.split(': ')
        c1, c2 = cs.split('|')
        c1 = [int(x) for x in c1.split()]
        c2 = [int(x) for x in c2.split()]
        c = len(set(c1) & set(c2))
        for j in range(c):
            d[i+j+1] += d[i]
    print(sum(d.values()))
    
if __name__ == '__main__':
    import sys
    
    with open('4.in') as f: 
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
