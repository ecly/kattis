l, e = [int(i) for i in input().split()]
rejected = 0
current = 0
for _ in range(e):
    action, size_ = input().strip().split()
    size = int(size_)
    if action == "enter":
        if current + size > l:
            rejected += 1
        else:
            current += size
    else:
        current -= size

print(rejected)
