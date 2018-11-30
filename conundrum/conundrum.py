cipher = input().strip()
per = "PER" * int(len(cipher)/3)
print(sum(int(x != y) for x, y in zip(cipher, per)))
