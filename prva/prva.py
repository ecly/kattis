r, _ = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(input())

words = []
for r in grid:
    words.extend(filter(lambda w: len(w) >= 2, r.split("#")))

for c in map(list, zip(*grid)):
    s = "".join(c)
    words.extend(filter(lambda w: len(w) >= 2, s.split("#")))

print(sorted(words)[0])
