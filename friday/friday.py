t = int(input())
for _ in range(t):
    d, m = [int(x) for x in input().split()]
    dim = [int(x) for x in input().split()]
    count = 0
    for i in range(len(dim)):
        if dim[i] < 13:
            continue
        days = sum(dim[:i])+13
        if days % 7 == 6:
            count += 1

    print(count)
