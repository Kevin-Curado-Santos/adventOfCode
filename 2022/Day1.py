arr = []
with open('input.txt') as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        line = line.strip()
        if line == '':
            arr.append(res)
            res = 0
        else:
            res += int(line)
    arr.append(res)
    
arr1 = sorted(arr)
print(max(arr1))
#sum last 3 elements
print(sum(arr1[-3:]))