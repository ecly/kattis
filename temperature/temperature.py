x, y = map(int, input().split())
if x == 0:
    print("ALL GOOD" if y == 1 else x)
else:
    catchup = -(y - 1)
    if catchup == 0:
        print("IMPOSSIBLE")
    else:
        print(x / catchup)
