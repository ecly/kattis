x = int(input())
if x < 100:
    print(99)
else:
    x += 1.1
    print((round(x/100)*100)-1)
