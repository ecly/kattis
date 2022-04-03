m = int(input())
targets = []
for _ in range(m):
    targets.append(tuple(map(int, input().split()[1:])))

n = int(input())
for _ in range(n):
    hits = 0
    x, y = map(int, input().split())
    for t in targets:
        if len(t) == 3:
            x1, y1, r = t
            d = (abs(x - x1)**2 + abs(y - y1)**2)**0.5
            if d <= r:
                hits += 1
        else:
            x1, y1, x2, y2 = t
            if x1 <= x <= x2 and y1 <= y <= y2:
                hits += 1

    print(hits)
