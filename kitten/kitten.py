K = int(input())
graph = dict()
while True:
    x = input()
    if x == "-1":
        break

    nodes = list(map(int, x.split()))
    parent = nodes[0]
    for i in nodes[1:]:
        graph[i] = parent


path = [K]
while True:
    if path[-1] not in graph:
        break
    path.append(graph[path[-1]])

print(" ".join(str(x) for x in path))
