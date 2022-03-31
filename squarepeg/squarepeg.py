import math
l, r = map(int, input().split())
print("fits" if math.sqrt(2) * r > l else "nope")
