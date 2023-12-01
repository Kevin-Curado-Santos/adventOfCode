data = set()

while True:
    try:
        line = input().split(' -> ')
        for i in range(len(line)-1):
            a, b = line[i].split(','), line[i+1].split(',')
            x, x1 = int(a[0]), int(b[0])
            x2, x3 = int(a[0])+1, int(b[0])+1
            y, y1 = int(a[1]), int(b[1])
            y2, y3 = int(a[1])+1, int(b[1])+1
            for j in range(min(x,x1), max(x2,x3)):
                for k in range(min(y,y1), max(y2,y3)):
                    data.add((j,k))
    except EOFError:
        break


# Part 1     
# initial = len(data)
# final = 0
# max_i = 1000
# i = 0
# while i < max_i:
#     a, b = 500, 0
#     c = 0
#     i +=1

#     while c < 1000:
#         c+=1
#         if (a,b+1) not in data:
#             b+=1
#             continue
#         else:
#             if (a-1,b+1) not in data:
#                 a-=1
#                 b+=1
#                 continue
#             elif (a+1,b+1) not in data:
#                 a+=1
#                 b+=1
#                 continue
#         data.add((a,b))
#         break
#     final = len(data)
    

# print(final-initial)
