from operator import itemgetter

for _ in range(int(input())):
    n = int(input())
    numbers = list(range(1, n + 1))
    mapping = {}
    for i in range(1, n + 1):
        for _ in range(i):
            numbers.append(numbers.pop(0))

        mapping[i] = numbers.pop(0)

    print(" ".join(str(k) for k, _ in sorted(mapping.items(), key=itemgetter(1))))
