from collections import Counter
m, n = map(int, input().split())
word_scores = {}
for _ in range(m):
    word, score = input().split()
    word_scores[word] = int(score)


for _ in range(n):
    counter = Counter()
    while True:
        x = input()
        if x == ".":
            break

        counter.update(x.split())

    score = 0
    for word, count in counter.items():
        score += count * word_scores.get(word, 0)


    print(score)
