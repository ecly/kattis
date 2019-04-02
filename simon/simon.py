T = int(input())
for _ in range(T):
    line = input()
    if line.startswith("simon says"):
        print(line[11:])
    else:
        print()
