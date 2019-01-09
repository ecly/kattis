n = int(input())
count = 0
for _ in range(n):
    line = input()
    if not "CD" in line:
        count += 1

print(count)
