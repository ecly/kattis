r, f = map(int, input().split())
rotation = (180 / r * f) % 360
print("down" if 90 < rotation < 270 else "up")
