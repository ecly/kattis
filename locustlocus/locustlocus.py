from math import gcd
# math.lcm is only available in python 3.9
# and kattis uses 3.8
def lcm(a, b):
    return (a // gcd(a, b)) * b


k = int(input())
reappearences = []
for _ in range(k):
    y, c1, c2 = map(int, input().split())
    reappearences.append(y + lcm(c1, c2))

print(min(reappearences))
