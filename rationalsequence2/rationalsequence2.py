P = int(input())
for _ in range(P):
    K, eq = input().split()
    p, q = map(int, eq.split("/"))
    d = 0
    path = []
    while p != 1 or q != 1:
        d += 1
        if p > q:
            p, q = p - q, q
            path.append(1)
        else:
            p, q = p, q - p
            path.append(0)

    base = 2 ** d
    offset = 0
    for idx, step in enumerate(path[::-1]):
        offset *= 2
        offset = max(0, offset + step)

    print(K, base + offset)
