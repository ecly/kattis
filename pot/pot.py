total = 0
for _ in range(int(input())):
    l = input()
    p = int(l[:-1])
    powi = int(l[-1])
    total += p**(powi)

print(total)
