def conversion(string):
    res = 0
    for c in string:
        res+=ord(c)
        res*=17
        res%=256
    return res

def part1(f):
    data = f.read().split(',')
    ans = 0
        
    for string in data:
        ans+=conversion(string)
        
    print(ans)

def part2(f):
    from collections import defaultdict
    box = defaultdict(dict)
    data = f.read().split(',')
    ans = 0
    
    for c in data:
        if c[-1] == "-":
            s = c[:-1]
            box[conversion(s)].pop(c[:-1], None)
        else:
            s = c[:-2]
            box[conversion(s)].update({c[:-2] : int(c[-1])})
            
    for k, v in box.items():
        for i, j in enumerate(v):
            ans += (k+1) * (i+1) * v[j]

    print(ans)

if __name__ == '__main__':
    import sys

    with open('15.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
