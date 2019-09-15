P, T = map(int, input().split())
solved = 0
for _ in range(P):
    success = True
    for _ in range(T):
        case = input()
        anthony = case[0].lower() + case[1:]
        if anthony != case.lower():
            success = False

    if success:
        solved += 1

print(solved)
