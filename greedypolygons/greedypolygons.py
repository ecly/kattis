import math


def cot(x):
    # no cotangent in python
    # https://github.com/python/cpython/issues/100943
    return math.cos(x) / math.sin(x)


n = int(input())
for _ in range(n):
    n, l, d, g = map(int, input().split())
    # n gon area formula
    # https://www.omnicalculator.com/math/regular-polygon-area
    base_area = n * l**2 * cot(math.pi / n) / 4
    new_square_area = n * l * d * g
    new_corner_area = (d * g) * (d * g) * math.pi
    total_area = base_area + new_square_area + new_corner_area
    print(total_area)
