import heapq
from itertools import product


def solve(grid, drain_coords):
    seen = {drain_coords}
    drain_level = grid[drain_coords]
    heap = [(drain_level, drain_coords)]
    flow = 0
    while heap:
        level, (row, col) = heapq.heappop(heap)
        flow += abs(level)
        for d_row, d_col in product([-1, 0, 1], [-1, 0, 1]):
            n_coords = row + d_row, col + d_col
            n_level = grid.get(n_coords, 0)

            if (n_level >= 0) or n_coords in seen:
                continue

            seen.add(n_coords)
            heapq.heappush(heap, (max(level, n_level), n_coords))

    return flow


def main():
    h, _w = map(int, input().split())
    grid = {}
    for row in range(1, h + 1):
        for col, altitude in enumerate(map(int, input().split()), 1):
            grid[row, col] = altitude

    i, j = map(int, input().split())
    print(solve(grid, (i, j)))


if __name__ == "__main__":
    main()
