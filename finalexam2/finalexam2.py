n = int(input())
answers = [input() for _ in range(n)]
print(sum(x == y for x, y in zip(answers, answers[1:])))
