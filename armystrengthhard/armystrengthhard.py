T = int(input())
for _ in range(T):
    _blank = input()
    _ng, _nm = map(int, input().split())
    godzilla = list(sorted(map(int, input().split())))
    mecha_godzilla = list(sorted(map(int, input().split())))
    if max(godzilla) >= max(mecha_godzilla):
        print("Godzilla")
    else:
        print("MechaGodzilla")
