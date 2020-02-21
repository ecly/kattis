def count_disjoint(graph, endpoints):
    seen = set()
    count = 0
    for e in range(endpoints):
        if e not in seen:
            count += 1

        queue = [e]
        while queue:
            node = queue.pop(0)
            seen.add(node)
            neighbors = graph[node]
            queue.extend([n for n in neighbors if n not in seen])

    return count


def main():
    cities = int(input())
    for _ in range(cities):
        endpoints = int(input())
        graph = {i: set() for i in range(endpoints)}
        roads = int(input())
        for _ in range(roads):
            start, end = map(int, input().split())
            graph[start].add(end)
            graph[end].add(start)

        print(count_disjoint(graph, endpoints) - 1)


if __name__ == "__main__":
    main()
