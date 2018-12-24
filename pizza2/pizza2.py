import math
R, C = list(map(int, input().split()))
size = R**2 * math.pi
size_no_crust = (R-C)**2 * math.pi
print(size_no_crust / size * 100)
