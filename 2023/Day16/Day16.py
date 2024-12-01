def go(grid, start):
    from collections import deque
    
    seen = set()
    q = deque([start])
        
    while q:
        x, y, dx, dy = q.popleft()
        
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            continue
        char = grid[x][y]
        if char == '.':
            if (x, y, dx, dy) not in seen:
                seen.add((x, y, dx, dy))
                q.append((x, y, dx, dy))
        elif char == '-' and dy != 0:
            if (x, y, dx, dy) not in seen:
                seen.add((x, y, dx, dy))
                q.append((x, y, dx, dy))
        elif char == '|' and dx != 0:
            if (x, y, dx, dy) not in seen:
                seen.add((x, y, dx, dy))
                q.append((x, y, dx, dy))    
        elif char == '/':
            if (x, y, -dy, -dx) not in seen:
                seen.add((x, y, -dy, -dx))
                q.append((x, y, -dy, -dx))
        elif char == '\\':
            if (x, y, dy, dx) not in seen:
                seen.add((x, y, dy, dx))
                q.append((x, y, dy, dx))
        else: 
            if char == '|':
                for dx, dy in [(1, 0), (-1, 0)]:
                    if (x, y, dx, dy) not in seen:
                        seen.add((x, y, dx, dy))
                        q.append((x, y, dx, dy))
            else:
                for dx, dy in [(0, 1), (0, -1)]:
                    if (x, y, dx, dy) not in seen:
                        seen.add((x, y, dx, dy))
                        q.append((x, y, dx, dy))
        
    coords = {(x, y) for x, y, _, _ in seen}            
    return len(coords)
    
def part1(f):
    data = f.read().splitlines()
    print(go(data, (0, -1, 0, 1)))

def part2(f):
    data = f.read().splitlines()
    ans = 0
    max_v = 0
    for i in range(len(data)):
        max_v = max(max_v, go(data, (i, -1, 0, 1))) # check every row starting from the left going to the right
        max_v = max(max_v, go(data, (i, len(data[0]), 1, 0))) # check every row starting from the right going to the left
    
    for i in range(len(data[0])):
        max_v = max(max_v, go(data, (-1, i, 1, 0))) # check every column starting from the top going to the bottom
        max_v = max(max_v, go(data, (len(data), i, -1, 0))) # check every column starting from the bottom going to the top
    
    print(max_v)

if __name__ == '__main__':
    import sys

    with open('16.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
