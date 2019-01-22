e, f, c = map(int, input().split())
total = 0
bottles = e + f
while bottles >= c:
    drank, left = divmod(bottles, c)
    total += drank
    bottles = drank + left

print(total)
