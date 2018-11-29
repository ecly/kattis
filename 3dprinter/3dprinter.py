import math
n = int(input())
printers = 1
printed = 0
days = 0
while printed < n:
    if n - printed > printers:
        printers *= 2
    else:
        printed += printers

    days += 1

print(days)
