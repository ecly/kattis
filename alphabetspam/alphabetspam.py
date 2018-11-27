chars = [ord(x) for x in input().strip()]
total = len(chars)
upper = len([x for x in chars if 64 < x < 91])
lower = len([x for x in chars if 96 < x < 123])
white = chars.count(95)
symbol = total - upper - lower - white
print(white / total)
print(lower / total)
print(upper / total)
print(symbol / total)
