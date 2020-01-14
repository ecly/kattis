n = int(input())
if n % 2 == 0:
    if n // 2 % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Either")
