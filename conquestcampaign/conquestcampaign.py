R, C, N = list(map(int, input().split()))

grid = set()
for _ in range(N):
    x, y = list(map(int, input().split()))
    grid.add((x, y))


def neighbors(x, y):
    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    return [
        (x + dx, y + dy) for dx, dy in offsets if 1 <= x + dx <= R and 1 <= y + dy <= C
    ]


days = 1
while len(grid) < R * C:
    days += 1
    grid = grid | set([n for x, y in grid for n in neighbors(x, y)])

print(days)
