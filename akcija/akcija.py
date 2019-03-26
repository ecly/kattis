import sys
prices = sorted(map(int, sys.stdin.readlines()[1:]), reverse=True)
free = prices[2::3]
print(sum(prices) - sum(free))
