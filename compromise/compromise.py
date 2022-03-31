from collections import Counter
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    answers = [input() for _ in range(n)]
    most_common_answers = []
    for i in range(m):
        a, _ = Counter([a[i] for a in answers]).most_common(1)[0]
        most_common_answers.append(a)

    print("".join(most_common_answers))
