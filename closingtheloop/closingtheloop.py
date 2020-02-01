for i in range(1, int(input()) + 1):
    s = int(input())
    ropes = input().split()
    reds = sorted([int(r[:-1]) for r in ropes if r[-1] == "R"])
    blues = sorted([int(r[:-1]) for r in ropes if r[-1] == "B"])
    knots = list(zip(reds[::-1], blues[::-1]))
    length = sum(sum(pair) for pair in knots) - len(knots) * 2 if knots else 0
    print(f"Case #{i}: {length}")
