import sys
sum = 0
for l in sys.stdin.readlines()[1:]:
    q, y = [float(x) for x in l.split()]
    sum += q * y

print(sum)
