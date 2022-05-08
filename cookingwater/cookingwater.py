from functools import reduce
n = int(input())
look_aways = [tuple(map(int, input().split())) for _ in range(n)]
sets = [set(range(a, b + 1)) for a, b in look_aways]
seconds_always_looked_away = reduce(set.intersection, sets[1:], sets[0])
print("gunilla has a point" if seconds_always_looked_away else "edward is right")
