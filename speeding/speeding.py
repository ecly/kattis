n = int(input())
photos = [tuple(map(int, input().split())) for _ in range(n)]
max_speed = 0
for (t1, d1), (t2, d2) in zip(photos, photos[1:]):
    max_speed = max(max_speed, (d2 - d1) // (t2 - t1))

print(max_speed)
