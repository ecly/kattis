a, b, c = map(int, input().split())
if a / b == c:
    print("%d/%d=%d" % (a, b, c))
elif a == b / c:
    print("%d=%d/%d" % (a, b, c))
elif a * b == c:
    print("%d*%d=%d" % (a, b, c))
elif a == b * c:
    print("%d=%d*%d" % (a, b, c))
elif a - b == c:
    print("%d-%d=%d" % (a, b, c))
elif a == b - c:
    print("%d=%d-%d" % (a, b, c))
elif a + b == c:
    print("%d+%d=%d" % (a, b, c))
elif a == b + c:
    print("%d=%d+%d" % (a, b, c))
