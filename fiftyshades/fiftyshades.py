n = int(input())
shows_to_attend = 0
for _ in range(n):
    name = input().lower()
    if "rose" in name or "pink" in name:
        shows_to_attend += 1

print(shows_to_attend if shows_to_attend else "I must watch Star Wars with my daughter")
