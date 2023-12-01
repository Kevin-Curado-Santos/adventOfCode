# Part 1

# data = []
# while True:
#     try:
#         a,b = input(), input()
#         data.append([eval(a),eval(b)])
#         _ = input()
#     except EOFError:
#         break


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return a - b
        else:
            return compare([a], b)
    
    else:
        if type(b) == int:
            return compare(a, [b])
        
    for x, y in zip(a, b):
        c = compare(x, y)
        if c:
            return c
        
    return len(a) - len(b)

# p1 = 0

# for i, (a,b) in enumerate(data):
#     if compare(a, b) < 0:
#         p1 += i + 1
        
# print(p1)


# Part 2
data2 = []
while True:
    try:
        a = input()
        if a == '':
            continue
        data2.append(eval(a))
    except EOFError:
        break

idx1 = 1
idx2 = 2
for elem in data2:
    if compare(elem, [[2]]) < 0:
        idx1 += 1
        idx2 += 1
    elif compare(elem, [[6]]) < 0:
        idx2 += 1

print(idx1*idx2)