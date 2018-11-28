import sys, math
for l in sys.stdin.readlines()[1:]:
    print(str(math.factorial(int(l)))[-1])
