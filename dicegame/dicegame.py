avg1 = sum(list(map(int, input().split()))) / 2
avg2 = sum(list(map(int, input().split()))) / 2
if avg1 == avg2:
    print("Tie")
else:
    print("Gunnar" if avg1 > avg2 else "Emma")
