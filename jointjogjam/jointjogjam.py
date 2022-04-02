ns = list(map(int, input().split()))
def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print(max(dist(*ns[:4]), dist(*ns[4:])))
