n = int(input())
birthdays = {}
for _ in range(n):
    name, rank, birthday = input().strip().split()
    rank = int(rank)
    if birthday not in birthdays or rank > birthdays[birthday][1]:
        birthdays[birthday] = (name, rank)

print(len(birthdays))
for name, _ in sorted(birthdays.values()):
    print(name)
