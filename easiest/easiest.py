import sys, math

def get_digit(n, i):
    return n // 10**i % 10

#https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
def int_len(n):
    return int(math.log10(n))+1

def get_sum(n):
    total = 0
    for i in range(int_len(n)):
        total += get_digit(n, i)

    return total

def match(n, p):
    return get_sum(n) == get_sum(n*p)


cases = [int(x) for x in sys.stdin.readlines()[:-1]]
for n in cases:
    p = 11
    while not match(n, p):
        p += 1

    print(p)
