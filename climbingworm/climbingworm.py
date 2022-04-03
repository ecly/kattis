a, b, h = map(int, input().split())
y = 0
climbs = 0
while y < h:
    y = max(0, y - b)
    climbs += 1
    y += a

print(climbs)
