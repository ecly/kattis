import sys
print(len(list(filter(lambda x: int(x) < 0, sys.stdin.readlines()[1].split()))))
