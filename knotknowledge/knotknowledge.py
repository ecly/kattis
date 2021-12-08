_ = int(input())
x = set(map(int, input().split()))
y = set(map(int, input().split()))
print(x.difference(y).pop())
