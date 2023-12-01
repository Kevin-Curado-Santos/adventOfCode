data = []
while True:
    try:
        _input = input().split()
        data.append(_input)
    except EOFError:
        break
# Part 1

cycles = [x for x in range(20, 301, 40)]

def check_cycle(cycle, x):
    if cycle in cycles:  
        return x*cycle
    else:
        return 0

cycle = 1
x = 1
ss = 0

for i in range(len(data)):
    if data[i][0] == "noop":
        ss += check_cycle(cycle, x)
        cycle += 1
    else:
        ss += check_cycle(cycle, x)
        cycle += 1
        ss += check_cycle(cycle, x)
        cycle += 1
        x += int(data[i][1])
     
print(ss)

# Part 2

# x = [1, 2, 3]
# screen = []
# cycle = 1

# def draw_pixel(x, cycle):
#     if cycle%40 in x:
#         screen.append('#')
#     else:
#         screen.append('.')

# for line in data:
#     if line[0] == "noop":
#         draw_pixel(x, cycle)
#         cycle += 1
#     else:
#         draw_pixel(x, cycle)
#         cycle += 1
#         draw_pixel(x, cycle)
#         cycle += 1
#         x = [x + int(line[1]) for x in x]

# for i in range(0, len(screen), 40):
#     print(''.join(screen[i:i+40]))

# x = 1
# screen = []

# for line in data:
#     if line[0] == "noop":
#         screen.append(x)
#     else:
#         screen.append(x)
#         screen.append(x)
#         x += int(line[1])
        
# for i in range(0, len(screen), 40):
#     for j in range(40):
#         print(end = "#" if abs(screen[i + j] - j) <= 1 else ".")
#     print()
