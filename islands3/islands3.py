from collections import deque


def minimum_islands(grid):
    seen = set()
    islands = 0
    for pos, type_ in grid.items():
        if type_ in "WC" or pos in seen:
            continue

        islands += 1
        seen.add(pos)
        queue = deque([pos])
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) in seen or grid.get((nx, ny), "W") == "W":
                    continue

                seen.add((nx, ny))
                queue.append((nx, ny))

    return islands


def main():
    r, _c = map(int, input().split())
    grid = {}
    for y in range(r):
        for x, v in enumerate(input()):
            grid[x, y] = v

    print(minimum_islands(grid))


if __name__ == "__main__":
    main()
