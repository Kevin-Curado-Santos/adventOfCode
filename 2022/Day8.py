with open('input.txt') as f:
    data = f.read().split()
    data = [list(map(int, x)) for x in data]      

count = 0

# Part 1
for r in range(len(data)):
    for c in range(len(data[r])):
        tree = data[r][c]
        if all(data[r][x] < tree for x in range(c)) or all(data[r][x] < tree for x in range(c+1, len(data[r]))) or all(data[x][c] < tree for x in range(r)) or all(data[x][c] < tree for x in range(r+1, len(data))):
            count += 1

print(count)

# Part 2

count2 = 0
for r in range(len(data)):
    for c in range(len(data[r])):
        tree = data[r][c]
        L, R, U, D = 0, 0, 0, 0
        for x in range(c-1, -1, -1):
            L+=1
            if data[r][x] >= tree:
                break
        for x in range(c+1, len(data[r])):
            R+=1
            if data[r][x] >= tree:
                break
        for x in range(r-1, -1, -1):
            U+=1
            if data[x][c] >= tree:
                break
        for x in range(r+1, len(data)):
            D+=1
            if data[x][c] >= tree:
                break
        count2 = max(count2, L*R*U*D)
        
print(count2)