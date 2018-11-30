i = input().split()
b = i[1]
n = int(i[0])

def get_points(number, s):
    scores = {"A": (11, 11),
              "K": (4, 4),
              "Q": (3, 3),
              "J": (20, 2),
              "T": (10, 10),
              "9": (14, 0),
              "8": (0, 0),
              "7": (0, 0)
              }

    if s == b:
        return scores[number][0]

    return scores[number][1]

total = 0
for _ in range(n * 4):
    line = input()
    total += get_points(line[0], line[1])

print(total)
