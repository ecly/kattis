n = int(input())
while True:
    names = []
    for _ in range(n):
        names.append(input())

    names.sort(key=lambda l: l[:2])
    print("\n".join(names))

    n = int(input())
    if n != 0:
        print()
    else:
        exit(0)
