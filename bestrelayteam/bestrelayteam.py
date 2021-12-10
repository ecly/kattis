from itertools import permutations
n = int(input())
runners = dict()
for _ in range(n):
    name, first, other = input().split()
    first, other = float(first), float(other)
    runners[name] = first, other

options = set()
for f in sorted(runners.items(), key=lambda x: x[1][0])[:5]:
    options.add(f)
for f in sorted(runners.items(), key=lambda x: x[1][1])[:5]:
    options.add(f)

def score_perm(perm):
    total_time = 0
    total_time = perm[0][1][0]
    for p in perm[1:]:
        total_time += p[1][1]

    return total_time

perms = permutations(options, r=4)
perms = sorted([(score_perm(perm), perm) for perm in perms])
score, runners = perms[0]
print(score)
print(runners[0][0])
print("\n".join(p[0] for p in sorted(runners[1:], key=lambda x: x[1][1])))
