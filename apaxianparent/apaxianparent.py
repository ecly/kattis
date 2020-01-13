y, p = input().split()
if y.endswith("e"):
    print(f"{y}x{p}")
elif y[-1] in "aiou":
    print(f"{y[:-1]}ex{p}")
elif y.endswith("ex"):
    print(f"{y}{p}")
else:
    print(f"{y}ex{p}")
