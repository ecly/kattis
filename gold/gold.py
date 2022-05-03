import sys
from collections import deque


def bfs(px, py, grid):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(px, py)])
    seen = set()
    gold = 0
    while queue:
        x, y = queue.popleft()
        neighbors = [(x + dx, y + dy) for dx, dy in d]
        neighbors = [(n, grid.get(n)) for n in neighbors]
        if any(c == "T" for _, c in neighbors):
            continue

        for (nx, ny), c in neighbors:
            if (nx, ny) in seen:
                continue

            seen.add((nx, ny))
            if c in "T#":
                continue

            if c == "G":
                gold += 1

            queue.append((nx, ny))

    return gold


def main():
    _w, h = map(int, sys.stdin.readline().split())
    grid = {}
    for y in range(h):
        for x, c in enumerate(sys.stdin.readline().rstrip()):
            grid[x, y] = c

    px, py = next(((x, y) for ((x, y), c) in grid.items() if c == "P"))
    no_risk_gold = bfs(px, py, grid)
    print(no_risk_gold)


if __name__ == "__main__":
    main()
