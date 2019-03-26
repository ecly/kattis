h, w, n = map(int, input().split())
bricks = map(int, input().split())

current_height = 0
current_width = 0
for b in bricks:
    current_width += b

    if current_width > w:
        break

    if current_width == w:
        current_width = 0
        current_height += 1

    if current_height == h:
        print("YES")
        exit(0)

print("NO")
