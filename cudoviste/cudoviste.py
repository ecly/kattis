R, C = list(map(int, input().split()))

grid = []
for r in range(R):
    grid.append([])
    row = input()
    for c in row:
        grid[r].append(c)

scores = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
for r in range(R - 1):
    for c in range(C - 1):
        spaces = grid[r][c] + grid[r][c + 1] + grid[r + 1][c] + grid[r + 1][c + 1]
        if any(c == "#" for c in spaces):
            continue
        cars = spaces.count("X")
        scores[cars] = scores[cars] + 1

for _, k in sorted(scores.items()):
    print(k)
