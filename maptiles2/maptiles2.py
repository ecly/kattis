s = input()
zoom_level = len(s)
x, y = 0, 0

for i, v in enumerate(s, 1):
    d = 2**zoom_level // 2**i
    if v in "13":
        x += d
    if v in "23":
        y += d

print(zoom_level, x, y)
