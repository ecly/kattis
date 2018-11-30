import sys
lines = sys.stdin.readlines()
scores = list(map(lambda l: sum([int(x) for x in l.split()]), lines))
best = max(scores)
print(scores.index(best) + 1, best)
