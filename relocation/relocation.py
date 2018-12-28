N, Q = list(map(int, input().split()))
locations = {str(i): int(d) for i, d in enumerate(input().split(), 1)}
for _ in range(Q):
    query, x, y = input().split()
    if query == "1":
        locations[x] = int(y)
    else:
        print(abs(locations[x] - locations[y]))
