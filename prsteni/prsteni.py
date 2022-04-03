from fractions import Fraction

n = int(input())
ns = list(map(int, input().split()))
prev = Fraction(1, 1)
for a, b in zip(ns, ns[1:]):
    f = Fraction(a, b)
    prev *= f
    print(f"{prev.numerator}/{prev.denominator}")
