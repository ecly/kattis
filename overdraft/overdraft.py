n = int(input())
max_deficit = 0
balance = 0
for _ in range(n):
    balance += int(input())
    max_deficit = min(max_deficit, balance)

print(abs(max_deficit))
