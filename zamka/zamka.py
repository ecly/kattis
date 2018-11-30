import math
def get_digit(n, i):
    return n // 10**i % 10

def int_len(n):
    return int(math.log10(n))+1

def get_sum(n):
    total = 0
    for i in range(int_len(n)):
        total += get_digit(n, i)

    return total

l = int(input())
d = int(input())
x = int(input())

n = 10_000
m = 1
for i in range(l, d+1):
    if get_sum(i) == x:
        n = min(i, n)
        m = max(i, m)

print(n)
print(m)
