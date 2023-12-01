import networkx as nx

data = []
i = 0 
while True:
    try:
        data.append(input())
        i+=1
    except EOFError:
        break
    
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

# Part 1

grid = {
    (i, j): x
    for i, row in enumerate(data)
    for j, x in enumerate(row)
}

start, end = None, None

for p, c in grid.items():
    if c == 'S':
        start = p
        grid[p] = 'a'
    elif c == 'E':
        end = p
        grid[p] = 'z'
    

G = nx.DiGraph()
for (x, y), c in grid.items():
    for dx, dy in dirs:
        if (ord(grid.get((x+dx, y+dy), 'A')) <= ord(c) + 1):
            G.add_edge((x, y), (x+dx, y+dy))
            
print(nx.shortest_path_length(G, start, end))

# Part 2

def find_min(G, start, end):
    try:
        return nx.shortest_path_length(G, start, end)  
    except nx.NetworkXNoPath:
        return 10e9

ans = 10e9
for p, c in grid.items():
    if c == 'a':
        ans = min(ans, find_min(G, p, end)) # type: ignore
        
print(ans)