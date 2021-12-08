limits = list(zip("ABCDE", map(int, input().split()))) + [("F", 0)]
score = int(input())
print(next(c for c, s in limits if score >= s))
