import sys, math
for line in sys.stdin.readlines()[:-1]:
    D, V = list(map(int, line.split()))
    print((((-6 * V) / math.pi + D**3))**(1/3))
