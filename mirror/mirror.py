T = int(input())
for i in range(1, T + 1):
    R, C = map(int, input().split())
    m = []
    for r in range(R):
        m.append(list(input()))

    print("Test", i)
    for r in m[::-1]:
        print("".join(r[::-1]))
