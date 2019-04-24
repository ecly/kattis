N = int(input())
numbers = list(map(int, input().split()))
last = numbers[0]
gis = [last]
for i in range(1, N):
    n = numbers[i]
    if n > last:
        gis.append(n)
        last = n

print(len(gis))
print(" ".join(map(str, gis)))
