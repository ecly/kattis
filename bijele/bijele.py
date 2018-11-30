x = [1, 1, 2, 2, 2, 8]
print(" ".join([str(x-y) for x,y in zip(x, [int(i) for i in input().split()])]))
