def case(amount):
    numbers = []
    for _ in range(amount):
        numbers.append(input())

    numbers.sort()
    for i in range(len(numbers)):
        c = numbers[i]
        for j in range(i + 1, len(numbers)):
            if numbers[j].startswith(c):
                return "NO"

            break

    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
print(case(n))
