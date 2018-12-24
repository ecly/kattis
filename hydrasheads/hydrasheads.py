import sys
for line in sys.stdin.readlines()[:-1]:
    h, t = list(map(int, line.split()))
    moves = 0
    while h > 0 or t > 0:
        grow = (0, 0)
        if t > 1:
            t -= 2
            grow = (1, 0)
        elif h > 1:
            h -= 2
            grow = (0, 0)
        else:
            t -= 1
            grow = (0, 2)

        h, t = h+grow[0], t+grow[1]
        moves += 1

    print(moves)
