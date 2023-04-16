import math
import sys

_, m = map(int, input().split())
if m == 0:
    print(0)
    sys.exit(0)

sneezes = 1
while not math.log2(m).is_integer():
    l2 = math.log2(m)
    m -= 2**math.floor(l2)
    sneezes += 1

print(sneezes)
