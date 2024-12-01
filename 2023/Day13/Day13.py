def fm(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if all(a == b for a, b in zip(above, below)):
            return r
    return 0
        
def part1(f):
    data = f.read().split('\n\n')
    ans = 0
    for l in data:
        grid = l.splitlines()
        ans += 100 * fm(grid)
        transposed_grid = [''.join(row) for row in zip(*grid)]
        ans += fm(transposed_grid)
    print(ans)

def fm2(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        c1 = 0
        for x, y in zip(above, below):
            c2 = 0
            for a, b in zip(x, y):
                if a != b:
                    c2 += 1
            c1 += c2
        if c1 == 1:
            return r
    return 0

def part2(f):
    data = f.read().split('\n\n')
    ans = 0
    for l in data:
        grid = l.splitlines()
        ans += 100 * fm2(grid)
        transposed_grid = [''.join(row) for row in zip(*grid)]
        ans += fm2(transposed_grid)
    print(ans)

if __name__ == '__main__':
    import sys

    with open('13.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
