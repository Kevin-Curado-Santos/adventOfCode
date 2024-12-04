def parse():
    l = []
    with open("day4.in", "r") as f:
       l = f.read().splitlines()
    return l, len(l), len(l[0])

def part1():
    l, h, w = parse()
    ans = 0
    
    for y in range(h):
        for x in range(w):
            for dx, dy in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
                for i, c in enumerate("XMAS"):
                    nx = x + dx * i
                    ny = y + dy * i
                    if nx < 0 or nx >= w or ny < 0 or ny >= h or l[ny][nx] != c:
                        break
                else:
                    ans += 1
    return ans

def part2():
    l, h, w = parse()
    ans = 0
    
    for y in range(h):
        for x in range(w):
            if l[y][x] != "A" or y == 0 or y == h - 1 or x == 0 or x == w - 1:
                continue
            # if ((l[y-1][x-1] == "M" and l[y+1][x+1] == "S") or (l[y-1][x-1] == "S" and l[y+1][x+1] == "M")) and ((l[y-1][x+1] == "M" and l[y+1][x-1] == "S") or (l[y-1][x+1] == "S" and l[y+1][x-1] == "M")):
            #     ans += 1
            if {l[y-1][x-1], l[y+1][x+1]} == {"M", "S"} and {l[y-1][x+1], l[y+1][x-1]} == {"M", "S"}:
                ans += 1
    return ans  

if __name__ == "__main__":
    print(part1())
    print(part2())
