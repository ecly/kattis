def rank(roll):
    if roll in ("12", "21"):
        return 100
    if roll[0] == roll[1]:
        return 100 - (7 - int(roll[0]))

    return int("".join(sorted(roll, reverse=True)))


while True:
    s0, s1, r0, r1 = input().split()

    if s0 == "0":
        break

    rank1 = rank(s0 + s1)
    rank2 = rank(r0 + r1)

    if rank1 == rank2:
        print("Tie.")
    elif rank1 > rank2:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
