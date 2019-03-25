d = {k: v for k, v in zip("ABC", sorted(map(int, input().split())))}
print(" ".join(str(d[ch]) for ch in input()))
