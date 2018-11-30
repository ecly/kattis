n = int(input())
for _ in range(n):
    m = int(input())
    cities = set()
    for _ in range(m):
        cities.add(input().strip())

    print(len(cities))
