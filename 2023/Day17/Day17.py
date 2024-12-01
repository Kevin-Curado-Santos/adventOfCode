def part1(f):
    from collections import deque
    from heapq import heappush, heappop
    data = f.read().splitlines()
    grid = [list(map(int, l)) for l in data]
    seen = set()
    #q = deque([(0, 0, 0, 0, 0, 0)])
    q = [(0, 0, 0, 0, 0, 0)]
    
    ans = 0
    
    while q:
        # hl, x, y, dx, dy, n = q.popleft()
        hl, x, y, dx, dy, n = heappop(q)
        if y == len(grid[0]) - 1 and x == len(grid) - 1:
            print(hl)
            break
            
        if (x, y, dx, dy, n) in seen:
            continue
        seen.add((x, y, dx, dy, n))
        
        if n < 3 and (dx, dy) != (0, 0):
            x2 = x + dx
            y2 = y + dy
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                # q.append((hl + grid[x2][y2], x2, y2, dx, dy, n + 1))
                heappush(q, (hl + grid[x2][y2], x2, y2, dx, dy, n + 1))
        
        for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (a, b) != (dx, dy) and (a, b) != (-dx, -dy):
                x2 = x + a
                y2 = y + b
                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                    # q.append((hl + grid[x2][y2], x2, y2, a, b, 1))
                    heappush(q, (hl + grid[x2][y2], x2, y2, a, b, 1))
        
        #print(q)
    
    print(ans)

def part2(f):
    data = f.read().splitlines()
    ans = 0
    print(ans)

if __name__ == '__main__':
    import sys

    with open('17.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
