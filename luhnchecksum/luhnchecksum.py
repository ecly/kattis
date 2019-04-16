T = int(input())
for _ in range(T):
    input_ = list(input())
    total = sum(map(int, input_[::-2]))
    for c in list(map(int, list(input_[-2::-2]))):
        total += (
            c * 2
            if c < 5
            else sum(map(int, list(str(c * 2))))
        )

    print("PASS" if total % 10 == 0 else "FAIL")
