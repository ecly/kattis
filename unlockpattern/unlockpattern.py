import re, sys, math
pattern = re.sub("\s+", "", sys.stdin.read())

def idx_to_xy(i):
    y = i // 3
    x = i % 3
    return x, y

cx, cy = idx_to_xy(pattern.index("1"))
dist = 0
for i in range(2, 10):
    x, y = idx_to_xy(pattern.index(str(i)))
    dx = abs(cx - x)
    dy = abs(cy - y)
    if dy == 0 or dx == 0:
        dist += dx + dy
    else:
        dist += math.sqrt(dx**2 + dy**2)

    cx, cy = x, y

print(dist)
