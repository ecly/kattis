n = int(input())
d = {}
for i in range(n):
    for j, c in enumerate(map(int, input().split())):
        if c != -1:
            d[i,j] = c

print(len(d))
for (i,j), c in sorted(d.items()):
    print(i+1,j+1,c)
