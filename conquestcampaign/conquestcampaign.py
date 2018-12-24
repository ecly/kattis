from collections import deque
R, C, N = list(map(int, input().split()))

queue = deque()
for _ in range(N):
    x, y = list(map(int, input().split()))
    queue.append((x, y))

day = 0
seen = set(queue)
offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while queue:
    day += 1
    for _ in range(len(queue)):
        x, y = queue.pop()
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= R and 1 <= ny <= C and (nx, ny) not in seen:
                seen.add((nx, ny))
                queue.append((nx, ny))


print(day)
