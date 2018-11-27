import sys
lines = sys.stdin.readlines()
total = len(lines[1:]) * int(lines[0])
print(total - sum(map(lambda x: int(x), lines[2:])))
