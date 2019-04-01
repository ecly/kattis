C = int(input())
for _ in range(C):
    case = list(map(int, input().split()))
    N = case[0]
    grades = case[1:]
    avg = sum(grades) / N
    above_avg = len(list(filter(lambda n: n > avg, grades)))
    above_avg_pct = above_avg / N * 100
    print("%.3f%%" % above_avg_pct)
