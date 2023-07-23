n = int(input())
line = [input() for _ in range(n)]
c = int(input())
events = [input() for _ in range(c)]
for event in events:
    e = event.split()
    if e[0] == "leave":
        line.remove(e[1])
    else:
        _, a, b = e
        idx = line.index(b)
        line.insert(idx, a)

print(*line, sep="\n")
