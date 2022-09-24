import random
n = int(input())
sets = []
for _ in range(n):
    sets.append(input().split())

print("\n".join(random.choice(sets)))
