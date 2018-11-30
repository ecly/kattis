c = float(input())
l = int(input())
total = 0
for _ in range(l):
    wi, li = [float(x) for x in input().split()]
    total += wi*li*c

print(total)
