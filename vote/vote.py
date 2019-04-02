from collections import Counter
T = int(input())
for _ in range(T):
    n = int(input())
    votes = []
    for _ in range(n):
        votes.append(int(input()))

    total = sum(votes)
    sorted_votes = sorted(votes, reverse=True)

    winner = sorted_votes[0]
    runner_up = sorted_votes[1]
    if winner == runner_up:
        print("no winner")
    elif winner > total // 2:
        print("majority winner", votes.index(winner) + 1)
    else:
        print("minority winner", votes.index(winner) + 1)
