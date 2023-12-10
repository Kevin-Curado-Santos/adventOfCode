def part1(f):
    from collections import deque
    
    data = f.read().strip().splitlines()
    for r, re in enumerate(data):
        for c, ce in enumerate(re):
            if ce == "S":
                sc = c
                sr = r
                break
    
    s = {(sr, sc)}
    q = deque([(sr, sc)])
    
    while q:
        r, c = q.popleft()
        a = data[r][c]
        
        if r>0 and a in "|LJS" and data[r-1][c] in "|7F" and (r-1, c) not in s:
            s.add((r-1, c))
            q.append((r-1, c))
            
        if r<len(data)-1 and a in "|7FS" and data[r+1][c] in "|LJ" and (r+1, c) not in s:
            s.add((r+1, c))
            q.append((r+1, c))
            
        if c>0 and a in "-J7S" and data[r][c-1] in "-LF" and (r, c-1) not in s:
            s.add((r, c-1))
            q.append((r, c-1))
            
        if c<len(data[r])-1 and a in "-LFS" and data[r][c+1] in "-J7" and (r, c+1) not in s:
            s.add((r, c+1))
            q.append((r, c+1))
            
    print(len(s)//2)

def shoelace(ps):
    n = len(ps)
    return abs(sum(ps[i][0]*ps[(i+1)%n][1] - ps[i][1]*ps[(i+1)%n][0] for i in range(n)))/2

def part2(f):
    
    data = f.read().strip().splitlines()
    for r, re in enumerate(data):
        for c, ce in enumerate(re):
            if ce == "S":
                sc = c
                sr = r
                break
    
    s = [(sr, sc)]
    q = [(sr, sc)]
    
    while q:
        r, c = q.pop()
        a = data[r][c]
        
        if r>0 and a in "|LJS" and data[r-1][c] in "|7F" and (r-1, c) not in s:
            s.append((r-1, c))
            q.append((r-1, c))
            
        if r<len(data)-1 and a in "|7FS" and data[r+1][c] in "|LJ" and (r+1, c) not in s:
            s.append((r+1, c))
            q.append((r+1, c))
            
        if c>0 and a in "-J7S" and data[r][c-1] in "-LF" and (r, c-1) not in s:
            s.append((r, c-1))
            q.append((r, c-1))
            
        if c<len(data[r])-1 and a in "-LFS" and data[r][c+1] in "-J7" and (r, c+1) not in s:
            s.append((r, c+1))
            q.append((r, c+1))
    
    s.append(s.pop(1))
    a = shoelace(s)
    print(a - len(s)//2 + 1)
    
if __name__ == '__main__':
    import sys

    with open('10.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
