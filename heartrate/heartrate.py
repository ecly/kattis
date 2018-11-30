for _ in range(int(input())):
    l = input().split()
    b = float(l[0])
    p = float(l[1])

    bpm = 60 * b / p
    lo =  60 / (p / (b-1))
    hi =  60 / (p / (b+1))
    print(lo, bpm, hi)
