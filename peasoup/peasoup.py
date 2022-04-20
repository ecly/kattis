n = int(input())
for _ in range(n):
    k = int(input())
    name = input()
    items = {input() for _ in range(k)}
    if "pea soup" in items and "pancakes" in items:
        print(name)
        break
else:
    print("Anywhere is fine I guess")
