from collections import defaultdict
case = 0
while True:
    case += 1
    n = int(input())
    if n == 0:
        break
    animals = defaultdict(int)
    for _ in range(n):
        animal = input().lower().split()[-1]
        animals[animal] += 1

    print("List %d:" % case)
    for animal, count in sorted(animals.items()):
        print("%s | %d" % (animal, count))
