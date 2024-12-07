def parse():
    with open("day6.in", "r") as f:
        l = list(map(list, f.read().split("\n")))
        
    h = len(l)
    w = len(l[0])
    
    for r in range(w):
        for c in range(h):
            if l[r][c] == "^":
                sr, sc = r, c
        
    return l, h, w, sr, sc

def part1():
    l, h, w, sr, sc = parse()
    
    v = set()   
    v.add((sr, sc))
    d = 0
    r, c = sr, sc
    while True: 
        dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
        
        if 0 <= r + dr < w and 0 <= c + dc < h and l[r + dr][c + dc] == "#":
            d = (d + 1) % 4
        else:
            r, c = r + dr, c + dc
            
        if r < 0 or r >= w or c < 0 or c >= h:
            return len(v)
            
        v.add((r, c))
        
def part2():
    l, h, w, sr, sc = parse()
    ans = 0
    
    def loop(grid, y, x):
        seen = set()
        d = 0
        
        while True:
            n = (y, x, d)
            if n in seen:
                return True
            seen.add(n)
            dy, dx = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            if not(0 <= y+dy < w and 0 <= x+dx < h):
                break
            while grid[y+dy][x+dx] == "#":
                d = (d + 1) % 4
                dy, dx = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            x, y = x+dx, y+dy
            if y < 0 or y >= w or x < 0 or x >= h:
                break
        return False
    
    for r in range(h):
        for c in range(w):
            if l[r][c] == ".":
                temp = l[r][c]
                l[r][c] = "#"
                if loop(l, sr, sc):
                    ans += 1
                l[r][c] = temp
    
    return ans
        
                

if __name__ == "__main__":
    print(part1())
    print(part2())