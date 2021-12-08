n = int(input())
blocks = 1
size = 1
side_length = 1
while True:
    side_length += 2
    blocks += side_length * side_length
    if blocks > n:
        break
    size += 1

print(size)
