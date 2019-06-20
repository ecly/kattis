grid = [input() for _ in range(5)]

if sum(x.count("k") for x in grid) != 9:
    print("invalid")
    exit(0)

moves = [(1, 2), (-1, 2), (1, -2), (-1, -2),
         (2, 1), (-2, 1), (2, -1), (-2, -1)]

for i in range(5):
    for j in range(5):
        if grid[i][j] != "k":
            continue
        else:
            if any(grid[i+k][j+l] == "k" for k, l in moves if 0 <= i+k < 5 and 0 <= j+l < 5):
                print("invalid")
                exit(0)

print("valid")
