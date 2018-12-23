import math
x, y, x1, y1, x2, y2 = list(map(int, input().split()))
minx = min(abs(x - x1), abs(x - x2))
miny = min(abs(y - y1), abs(y - y2))
if y >= y1 and y <= y2:
    print(minx)
elif x >= x1 and x <= x2:
    print(miny)
else:
    print(math.sqrt(minx**2 + miny**2))
