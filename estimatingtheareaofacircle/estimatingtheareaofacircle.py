import sys, math
for line in sys.stdin.readlines()[:-1]:
    r, m, c = list(map(float, line.split()))
    real = r**2 * math.pi
    estimate = r * r * 4 * c / m
    print(real, estimate)
