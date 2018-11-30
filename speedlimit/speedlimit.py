while(True):
    n = int(input())
    if n == -1:
        break
    dist = 0
    last_elapsed = 0
    for _ in range(n):
        speed, time = [int(x) for x in input().split()]
        dist += speed * (time - last_elapsed)
        last_elapsed = time

    print(dist, "miles")
