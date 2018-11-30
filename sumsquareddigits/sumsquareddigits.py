import string
digs = string.digits + string.ascii_letters

# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-in-any-base-to-a-string
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

p = int(input())

hexa = {"a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15}

for _ in range(p):
    k, b, n = [int(x) for x in input().split()]
    total = 0
    for c in str(int2base(n, b)):
        if c in hexa:
            total+= hexa[c]**2
        else:
            total += int(c)**2

    print(k, total)
