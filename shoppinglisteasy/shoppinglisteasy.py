from functools import reduce
n, m = map(int, input().split())
lists = [set(input().split()) for _ in range(n)]
common = reduce(lambda x, y: x.intersection(y), lists[1:], lists[0])
print(len(common))
print("\n".join(sorted(common)))
