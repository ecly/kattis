target = set(input())
misses = 0
for c in input():
    if c in target:
        target.remove(c)
    else:
        misses += 1

    if misses == 10:
        break
    if not target:
        print("WIN")
        exit(0)

print("LOSE")
