# https://math.stackexchange.com/questions/1010591/what-is-the-number-of-intersections-of-diagonals-in-a-convex-equilateral-polygon
n = int(input())
print((n * (n - 1) * (n - 2) * (n - 3)) // 24)
