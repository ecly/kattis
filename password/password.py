import sys
ps = sorted(map(lambda l: float(l.split()[1]), sys.stdin.readlines()[1:]), reverse=True)
print(sum(p * i for p, i in zip(ps, range(1, len(ps) + 1))))
