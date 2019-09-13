import fileinput, functools

def gcd(x, y):
   while(y):
       x, y = y, x % y

   return x

def lcm(x, y):
   return (x * y) // gcd(x, y)

for l in fileinput.input():
    numbers = list(map(int, l.split()))
    print(int(functools.reduce(lcm, numbers[1:], numbers[0])))
