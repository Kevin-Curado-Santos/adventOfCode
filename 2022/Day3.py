a1 = {chr(i+96):i for i in range(1,27)}
a2 = {chr((i-26)+64):i for i in range(27,53)}
alphabet = {**a1, **a2}
with open('input.txt') as f:
    lines = f.readlines()
    length = len(lines)
    sum = 0
    i = 0
    while(i<length):
        
        c1 = lines[i].strip()
        c2 = lines[i+1].strip()
        c3 = lines[i+2].strip()
        d1 = {}
        d2 = {}
        d3 = {}
        for char in c1:
            if char not in d1:
                d1[char] = 1
        for char in c2:
            if char not in d2:
                d2[char] = 1
        for char in c3:
            if char not in d3:
                d3[char] = 1
        for item in d1.keys():
            if item in d2.keys() and item in d3.keys():
                sum += alphabet[item]
        i+=3
    print(sum)
