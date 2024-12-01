def tilt(grid):    
    for row in grid:
            s = 0
            for i,c in enumerate(row):
                if c == '#':
                    s = i + 1
                if c == 'O':
                    row[i] = '.'
                    row[s] = 'O'
                    s += 1

def part1(f):
    data = f.read().splitlines()
    grid = [list(l.strip()) for l in data]
    grid = [list(x) for x in zip(*grid)]
    
    tilt(grid)
    ans = sum(i + 1 for col in grid for i,c in enumerate(col[::-1]) if c == 'O')
    print(ans)

def part2(f):
    seen = {}
    data = f.read().splitlines()
    grid = [list(l.strip()) for l in data]
    for i in range(1000000000):
        grid = [list(x) for x in zip(*grid)]
        tilt(grid)
        grid = [list(x) for x in zip(*grid)]
        tilt(grid)
        grid = grid[::-1]
        grid = [list(x) for x in zip(*grid)]
        tilt(grid)
        grid = grid[::-1]
        grid = [list(x) for x in zip(*grid)]
        grid = [row[::-1] for row in grid]
        tilt(grid)
        grid = [row[::-1] for row in grid]
    grid = [list(x) for x in zip(*grid)]
        
    ans = sum(i + 1 for col in grid for i,c in enumerate(col[::-1]) if c == 'O')
    print(ans)

if __name__ == '__main__':
    import sys

    with open('14test.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
