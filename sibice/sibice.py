import math, sys
_, a, b = [int(x) for x in input().split()]
c = math.sqrt(a**2 + b**2)
for l in sys.stdin.readlines():
    print("DA" if int(l) <= c else "NE")
