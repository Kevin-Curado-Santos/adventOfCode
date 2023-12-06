def part1(f):
    data = f.read().strip().split('\n\n')
    s, data = list(map(int, data[0].split(': ')[1].split())), data[1:]
    
    for fm in data:
        r = [list(map(int, x.split())) for x in fm.splitlines()[1:]]
        
        l = [] # results of mapping 
        for x in s:
            for a, b, c in r:
                if b<=x and x<b+c:
                    l.append(x-b+a) # if there is mapping
                    break
            else:
                l.append(x) # if there is no mapping
        s = l # update s
    
    print(min(s))
        

def part2(f):
    data = f.read().strip().split('\n\n')
    sr, data = list(map(int, data[0].split(': ')[1].split())), data[1:]
    
    s = [(sr[i], sr[i]+sr[i+1]) for i in range(0, len(sr), 2)]
    
    for fm in data:
        r = [list(map(int, x.split())) for x in fm.splitlines()[1:]]
        
        l = [] # results of mapping 
        while s:
            st, ed = s.pop()
            for a, b, c in r:
                max_st = max(st, b)
                min_ed = min(ed, b+c)
                if max_st<min_ed:
                    l.append((max_st-b+a, min_ed-b+a)) # if there is mapping of the range
                    if max_st>st:
                        s.append((st, max_st)) # have to check the left part 
                    if ed>min_ed:
                        s.append((min_ed, ed)) # have to check the right part
                    break
            else:
                l.append((st, ed)) # if there is no mapping
        s = l # update s
    
    print(min(s)[0])
    
if __name__ == '__main__':
    import sys
    
    with open('5.in') as f: 
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
