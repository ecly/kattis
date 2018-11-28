n = input()
i = [int(x) for x in input().split() if x != "-1"]
print(sum(i) / len(i))
