from math import floor
from statistics import mean

print(chr(floor(mean([ord(c) for c in input()]))))
