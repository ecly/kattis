t = int(input())
for _ in range(t):
    seq = [int(i) for i in input().split()[:-1]]
    total = 0
    for l, h in zip(seq, seq[1:]):
        if l*2 < h:
            total += h - l * 2

    print(total)
