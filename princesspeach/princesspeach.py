N, Y = map(int, input().split())
found = set()
for _ in range(Y):
    found.add(int(input()))

for i in range(N):
    if i not in found:
        print(i)

print("Mario got %d of the dangerous obstacles." % len(found))
