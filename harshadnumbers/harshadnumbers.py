def is_harshad(number):
    total = sum(int(c) for c in str(number))
    return number % total == 0

n = int(input().strip())
while not is_harshad(n):
    n+=1

print(n)
