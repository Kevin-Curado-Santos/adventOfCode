def part1(f):
    data = f.read().strip().split('\n')
    ts = list(map(int, data[0].split(': ')[1].split()))
    ds = list(map(int, data[1].split(': ')[1].split()))

    r=1
    for t, d in zip(ts, ds):
        w = 0
        for i in range(1,t+1):
            if(t-i)*i > d:
                w+=1
        r *= w
    print(r)

def part2(f):
    data = f.read().strip().split('\n')
    t = int(''.join(data[0].split(': ')[1].split()))
    d = int(''.join(data[1].split(': ')[1].split()))

    w = 0
    for i in range(1, t+1):
        if(t-i)*i > d:
            w = i
            break
    print(t+1-2*w)

if __name__ == '__main__':
    import sys

    with open('6.in') as f:
        if sys.argv[1] == '1':
            part1(f)
        else:
            part2(f)
