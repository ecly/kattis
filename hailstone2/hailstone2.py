n = int(input())
sequence = [n]
while sequence[-1] != 1:
    last = sequence[-1]
    if last % 2 == 0:
        sequence.append(last // 2)
    else:
        sequence.append(last * 3 + 1)

print(len(sequence))
