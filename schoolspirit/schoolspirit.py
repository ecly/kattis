from statistics import mean
def score(scores_):
    return 1/5 * sum(s * (4/5)**i for i, s in enumerate(scores_))

n = int(input())
scores = [int(input()) for _ in range(n)]
scores.sort(reverse=True)
print(score(scores))
new_scores = []
for i in range(n):
    x = scores[:i] + scores[i+1:]
    new_scores.append(score(x))

print(mean(new_scores))
