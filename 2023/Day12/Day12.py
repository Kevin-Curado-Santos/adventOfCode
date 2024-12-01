from collections import defaultdict

dp = defaultdict(int)

def count_config(cs, ns):
    if cs == '':
        return 1 if len(ns) == 0 else 0
    if len(ns) == 0:
        return 0 if '#' in cs else 1
    
    if (cs, tuple(ns)) in dp:
        return dp[(cs, tuple(ns))]
    
    ans = 0
    
    if cs[0] in ".?":
        ans += count_config(cs[1:], ns)
    
    if cs[0] in "#?":
        if ns[0] <= len(cs) and (ns[0] == len(cs) or cs[ns[0]] != '#') and '.' not in cs[:ns[0]]:
            ans += count_config(cs[ns[0]+1:], ns[1:])
            
    dp[(cs, tuple(ns))] = ans
    return ans

def part1(f):
    data = f.read().splitlines()
    ans = 0
    for l in data:
        cs, ns = l.split()
        ns = list(map(int, ns.split(',')))
        ans += count_config(cs, ns)
        
    print(ans)

def part2(f):
    data = f.read().splitlines()
    ans = 0
    for l in data:
        cs, ns = l.split()
        ns = list(map(int, ns.split(',')))
        
        cs = "?".join([cs]*5)
        ns *= 5
        
        ans += count_config(cs, ns)
    print(ans)

if __name__ == '__main__':
    import sys

    with open('12.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
