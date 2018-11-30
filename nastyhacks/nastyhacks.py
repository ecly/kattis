for _ in range(int(input())):
    r, e, c = [int(x) for x in input().split()]
    if e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")
    else:
        print("does not matter")
