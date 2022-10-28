s = input()
ids = input()
ns = [int(ids[i:i+3]) for i in range(0, len(ids), 3)]
print("".join(s[n-1] for n in ns))
