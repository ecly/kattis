from collections import defaultdict
n = int(input())
while n != 0:
    items = defaultdict(list)
    for _ in range(n):
        input_ = input().split()
        name = input_[0]
        for item in input_[1:]:
            items[item].append(name)

    for item, names in sorted(items.items()):
        print(" ".join([item] + sorted(names)))

    print()
    n = int(input())
