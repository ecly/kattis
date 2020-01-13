n = int(input())
recited = {int(input()) for _ in range(n)}
all_numbers = set(range(1, max(recited) + 1))
missing = all_numbers.difference(recited)
if missing:
    print(*sorted(missing), sep="\n")
else:
    print("good job")
