def part1(f):
    data = f.read().splitlines()
    er = [i for i in range(len(data)) if all(data[i][j] == '.' for j in range(len(data[i])))]
    ec = [i for i in range(len(data[0])) if all(data[j][i] == '.' for j in range(len(data)))]
    g = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#']
    
    ans = 0
    
    for i,(r,c) in enumerate(g):
        for j in range(i, len(g)):
            r2, c2 = g[j]
            d = abs(r2-r) + abs(c2-c)
            for e in er:
                if min(r,r2) < e < max(r,r2):
                    d+=1
            for e in ec:
                if min(c,c2) < e < max(c,c2):
                    d+=1
            ans+=d
    print(ans)

def part2(f):
    data = f.read().splitlines()
    er = [i for i in range(len(data)) if all(data[i][j] == '.' for j in range(len(data[i])))]
    ec = [i for i in range(len(data[0])) if all(data[j][i] == '.' for j in range(len(data)))]
    g = [(i,j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == '#']
    
    ans = 0
    
    for i,(r,c) in enumerate(g):
        for j in range(i, len(g)):
            r2, c2 = g[j]
            d = abs(r2-r) + abs(c2-c)
            for e in er:
                if min(r,r2) < e < max(r,r2):
                    d+=10**6-1
            for e in ec:
                if min(c,c2) < e < max(c,c2):
                    d+=10**6-1
            ans+=d
    print(ans)

if __name__ == '__main__':
    import sys

    with open('11.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
