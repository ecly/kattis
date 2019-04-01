N = int(input())
names = []
for _ in range(N):
    names.append(input())

sorted_names = sorted(names)

if names == sorted_names:
    print("INCREASING")
elif names == sorted_names[::-1]:
    print("DECREASING")
else:
    print("NEITHER")
