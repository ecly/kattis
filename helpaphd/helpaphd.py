N = int(input())
for _ in range(N):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        print(sum(list(map(int, line.split("+")))))
