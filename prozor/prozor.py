R, S, K = list(map(int, input().split()))

grid = []
for i in range(R):
    grid.append([])
    for c in input():
        grid[i].append(c)

count = 0
coords = (0, 0)
for y in range(R - K + 1):
    rows = grid[y + 1 : y + K - 1]
    for x in range(S - K + 1):
        flies = sum(
            list(
                map(
                    lambda s: s.count("*"),
                    map(lambda l: "".join(l[x + 1 : x + K - 1]), rows),
                )
            )
        )
        if flies > count:
            coords = (y, x)
            count = flies

edge_y, edge_x = coords
for x in range(edge_x, edge_x + K):
    grid[edge_y][x] = "-"
    grid[edge_y+K-1][x] = "-"

for y in range(edge_y, edge_y + K):
    grid[y][edge_x] = "|"
    grid[y][edge_x+K-1] = "|"

grid[edge_y][edge_x] = "+"
grid[edge_y+K-1][edge_x] = "+"
grid[edge_y][edge_x+K-1] = "+"
grid[edge_y+K-1][edge_x+K-1] = "+"

print(count)
for row in grid:
    print(''.join(row))
