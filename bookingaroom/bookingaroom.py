r, n = list(map(int, input().split()))
rooms = {i for i in range(1, r + 1)}
for _ in range(n):
    rooms.remove(int(input()))

if rooms:
    print(rooms.pop())
else:
    print("too late")
