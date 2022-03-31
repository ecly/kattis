def is_weak(v, g):
    for n in g[v]:
        for nn in g[n]:
            if nn in g[v]:
                return False

    return True


def main():
    while True:
        n = int(input())
        if n == -1:
            break

        graph = {i: set() for i in range(n)}
        for r in range(n):
            for c, i in enumerate(input().split()):
                if i == "1":
                    graph[c].add(r)
                    graph[r].add(c)

        weak = [v for v in graph if is_weak(v, graph)]
        print(*sorted(weak))


if __name__ == "__main__":
    main()
