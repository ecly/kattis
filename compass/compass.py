n1 = int(input())
n2 = int(input())
diff = abs(n1 - n2)
if diff == 180:
    print(180)
elif diff > 180:
    if n1 > n2:
        print(360 - n1 + n2)
    else:
        print(-360 + n2 - n1)
else:
    print(n2 - n1)
