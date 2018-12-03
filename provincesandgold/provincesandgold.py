victory = [(8, 6, "Province"), (5, 3, "Duchy"), (2, 1, "Estate")]
treasure = [(6, 3, "Gold"), (3, 2, "Silver"), (0, 1, "Copper")]
g, s, c = [int(x) for x in input().split()]
power = g * 3 + s * 2 + c * 1
vic = [name for cost, _, name in victory if cost <= power]
tre = [name for cost, _, name in treasure if cost <= power]
if power < 2:
    print(tre[0])
else:
    print("%s or %s" % (vic[0], tre[0]))
