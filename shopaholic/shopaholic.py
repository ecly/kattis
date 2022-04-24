import sys

_ = int(sys.stdin.readline())
items = sorted(map(int, sys.stdin.readline().split()))
print(sum(items[-3::-3]))
