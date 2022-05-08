from functools import reduce
from operator import mul
x = int(input())
while x > 9:
    nums = [int(i) for i in str(x) if i != "0"]
    # math.prod only introduced in 3.8
    x = reduce(mul, nums, 1)

print(x)
