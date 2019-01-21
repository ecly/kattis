from math import sqrt
k = int(input())
#mathworld.wolfram.com/images/equations/FibonacciNumber/NumberedEquation6.gif
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

print(int(F(k-1)), int((F(k))))
