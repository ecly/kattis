W, _P = map(int, input().split())
L = list(map(int, input().split()))
possible = set([W])
for idx, p in enumerate(L):
    possible.add(p)
    possible.add(W - p)
    possible = possible | set(map(lambda l: abs(p - l), L[idx+1:]))

print(' '.join(map(str, sorted(possible))))
