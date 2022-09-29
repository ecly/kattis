c, k = map(int, input().split())

inc = 10**k
min_amount = (c // inc) * inc

# we check if the remaining amount should be rounded up or down
# accounting for python floating point errors, by adding an epsilon
rem = c - min_amount
print(min_amount + inc if round((rem / inc) + 1e-3) else min_amount)
