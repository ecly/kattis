seq = list(map(int, input().split()))
sorted_seq = sorted(seq)
while seq != sorted_seq:
    for i in range(4):
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
            print(*seq)
