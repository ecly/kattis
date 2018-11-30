import math
h, v = [int(x) for x in input().split()]
print(int(math.ceil(h / math.cos(math.radians(90-v)))))
