import math

a, b, c, d = map(int, input().split())
semiperimeter = (a + b + c + d) / 2
print(
    math.sqrt(
        (semiperimeter - a)
        * (semiperimeter - b)
        * (semiperimeter - c)
        * (semiperimeter - d)
    )
)
