import math
n = int(input())
for _ in range(n):
    v0, theta, x, h1, h2 = [float(i) for i in input().split()]

    t = x / (v0 * math.cos(math.radians(theta)))
    y = v0 * t * math.sin(math.radians(theta)) - 0.5 * 9.81 * t**2
    if y - 1.0 >= h1 and y + 1.0 <= h2:
        print("Safe")
    else:
        print("Not Safe")
