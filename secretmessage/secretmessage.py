import math
N = int(input())
for _ in range(N):
    msg = input()
    L = len(msg)
    M = math.ceil(math.sqrt(L))**2
    padded = msg + "*" * (M - L)
    table = []
    K = int(math.sqrt(M))
    for i in range(K):
        l = i * K
        h = l + K
        table.append(padded[l:h])

    out = ""
    for i in range(K):
        for j in range(K):
            out += table[K-1-j][i]

    print(out.replace("*", ""))
