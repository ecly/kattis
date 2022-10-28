from fractions import Fraction

fahrenheit = Fraction(input())
celsius = 5 * (fahrenheit - 32) / 9
print(*celsius.as_integer_ratio(), sep="/")
