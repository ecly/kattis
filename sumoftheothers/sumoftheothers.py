import fileinput
for line in fileinput.input():
    numbers = list(map(int, line.split()))
    total = sum(numbers)
    for n in numbers:
        if total - n == n:
            print(n)
            break
