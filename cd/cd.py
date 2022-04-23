from sys import stdin
while True:
    n, m = map(int, stdin.readline().split())
    if n == 0 and m == 0:
        break
    jack = {int(stdin.readline()) for _ in range(n)}
    jill = {int(stdin.readline()) for _ in range(m)}
    print(len(jack.intersection(jill)))
