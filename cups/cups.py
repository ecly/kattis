n = int(input())
cups = []
for _ in range(n):
   x, y = input().split()
   cups.append((int(x), y) if x.isdigit() else (int(y)*2, x))

for size, color in sorted(cups):
    print(color)
