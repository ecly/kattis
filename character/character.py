import math

n = int(input())
relationships = 0
for i in range(2, n + 1):
    relationships += math.factorial(n) // math.factorial(i) // math.factorial(n - i)

print(relationships)
