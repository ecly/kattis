import heapq
import sys


def prims(neighbors, n):
    tree = {0}
    dists = [1 << 30] * n
    fringe = []
    for j, d in enumerate(neighbors[0]):
        dists[j] = d
        heapq.heappush(fringe, (d, 0, j))

    while fringe and len(tree) < n:
        _, prev, node = heapq.heappop(fringe)
        if node in tree:
            continue

        tree.add(node)
        print(node + 1, prev + 1)

        for nb, d in enumerate(neighbors[node]):
            if nb in tree:
                continue

            if d >= dists[nb]:
                continue

            dists[nb] = d
            heapq.heappush(fringe, (d, node, nb))


def main():
    n = int(sys.stdin.readline())
    neighbors = []
    for _ in range(n):
        neighbors.append(list(map(int, sys.stdin.readline().rstrip().split())))

    prims(neighbors, n)


if __name__ == "__main__":
    main()
