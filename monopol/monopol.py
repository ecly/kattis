from itertools import product

_n = int(input())
an = list(map(int, input().split()))
rs = range(1,7,1)
cs = list(product(rs, rs))
print(sum(sum(dice) in an for dice in cs) / len(cs))
