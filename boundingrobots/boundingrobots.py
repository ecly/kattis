d = {"u": (0, 1), "d": (0, -1), "r": (1, 0), "l": (-1, 0)}
while True:
    w, l = map(int, input().split())
    if not (w and l):
        break

    px, py = 0, 0
    rx, ry = 0, 0
    n = int(input())
    for _ in range(n):
        x, y = input().split()
        dx, dy = d[x]
        dx, dy = dx * int(y), dy * int(y)
        px, py = max(0, min(w - 1, px + dx)), max(0, min(l - 1, py + dy))
        rx, ry = rx + dx, ry + dy

    print("Robot thinks", rx, ry)
    print("Actually at", px, py)
    print()
