import sys, collections
scores = collections.defaultdict(int)
total = 0
count = 0
for line in sys.stdin.readlines()[:-1]:
    time, question, answer = line.split()
    scores[question] += 20 if answer == "wrong" else int(time)
    if answer == "right":
        total += scores[question]
        count += 1

print(count, total)
