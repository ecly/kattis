from itertools import product

m, n = map(int, input().split())
grid = {}
for x in range(m):
    for y, c in enumerate(input()):
        grid[x, y] = c

seen = set()


ns = list(product((-1, 0, 1), repeat=2))
ns.remove((0, 0))


def mark_loop(sx, sy):
    q = [(sx, sy)]
    while q:
        x, y = q.pop(0)
        for nx, ny in ns:
            nx, ny = x + nx, y + ny
            if grid.get((nx, ny)) != "#" or (nx, ny) in seen:
                continue

            q.append((nx, ny))
            seen.add((nx, ny))


loops = 0
for (x, y), c in grid.items():
    if c != "#" or (x, y) in seen:
        continue

    mark_loop(x, y)
    loops += 1

print(loops)
