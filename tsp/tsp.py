import math
N = int(input())
points = []
for _ in range(N):
    x, y = map(float, input().split())
    points.append((x, y))

def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

tour = [0]
used = [False] * N
used[0] = True
for _ in range(N - 1):
    best = -1
    for j in range(N):
        if used[j]:
            continue
        if best == -1 or dist(tour[-1], j) < dist(tour[-1], best):
            best = j

    tour.append(best)
    used[best] = True

for i in tour:
    print(i)
