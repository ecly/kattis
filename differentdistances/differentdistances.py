import sys
for line in sys.stdin.readlines()[:-1]:
    x1, y1, x2, y2, p = list(map(float, line.split()))
    print((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p))
