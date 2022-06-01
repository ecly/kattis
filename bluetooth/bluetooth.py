n = int(input())
# track functional teeth in upper/lower, left/right region of mouth
jaw_sides = {"ul": 8, "ur": 8, "ll": 8, "lr": 8}
for _ in range(n):
    loc, state = input().split()
    idx = "u" if "+" in loc else "l"
    idx += "l" if loc[1].isdigit() else "r"
    jaw_sides[idx] -= 8 if state == "b" else 1

if jaw_sides["ul"] > 0 and jaw_sides["ll"] > 0:
    print(0)
elif jaw_sides["ur"] > 0 and jaw_sides["lr"] > 0:
    print(1)
else:
    print(2)
