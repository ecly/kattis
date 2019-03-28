_N = int(input())
numbers = sorted(map(int, input().split()))
groups = []
group = []
last = None
for number in numbers:
    if group and number - last != 1:
        groups.append(group)
        group = []

    group.append(str(number))
    last = number

groups.append(group)

print(' '.join(map(lambda g: ' '.join(g) if len(g) < 3 else "%s-%s" % (g[0], g[-1]), groups)))
