with open('input.txt') as f:
    stacks = []
    for _ in range(9):
        stacks.append([])

    line_list = []
    for _ in range(8):
        line = f.readline()
        line_list.append(line)
    line_list.reverse()

    for line in line_list:
        cnt = 0
        for i, character in enumerate(line):
            if i in [1, 5, 9, 13, 17, 21, 25, 29, 33]:
                if character.isupper():
                    stacks[cnt].append(character)
                cnt += 1
    
    
    data = f.readlines()[2:]
    data = [line.strip() for line in data]
    for line in data:
        arr = line.split()
        n, s, d = map(int, [x for x in arr if x.isdigit()])
        temp = stacks[s-1][-n:]
        del stacks[s-1][-n:]
        stacks[d-1].extend(temp)
        # part 1
        # for i in range(n):
        #    stacks[d-1].append(stacks[s-1].pop())
    
    print(''.join([x[-1] for x in stacks]))
    