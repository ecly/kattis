print(int(sum(int(a) * int(c) for a, c in zip("4327654321",  input().replace("-", ""))) % 11 == 0))
