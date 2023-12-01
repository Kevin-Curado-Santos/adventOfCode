def part1():
    import re

    ans=0
    while True:
        try:
            s = input()
            m=''.join(re.findall(r'\d+', s))
            if len(m)==1:
                m+=m
            elif len(m)>2:
                m=m[0]+m[-1]
            ans+=int(m)
        except EOFError:
            break
    print(ans)

def part2():
    nums = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()

    ans = 0
    while True:
        try:
            s = input()
            f = min(nums, key=lambda x: s.index(x) if x in s else 999)
            l = min(nums, key=lambda x: s[::-1].index(x[::-1]) if x in s else 999) 
            ans += nums.index(f) //2 * 10 + nums.index(l)//2
        except EOFError:
            break
        
    print(ans)
    
if __name__ == '__main__':
    import sys
    
    if sys.argv[1] == '1':
        part1()
    else:
        part2()