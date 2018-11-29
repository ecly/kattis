x, y, z = sorted([int(i) for i in input().split()])
if z - y == y - x:
    print(z + abs(z - y))
elif z - y > y - x:
    print(y + abs(y - x))
else:
    print(x + abs(z - y))
