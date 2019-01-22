n = int(input())
for _ in range(n):
    gnomes = list(map(int, input().split()[1:]))
    for i in range(len(gnomes) - 2):
        a, b, c = gnomes[i:i+3]
        if a < b > c and a < c:
            print(i + 2)
            break
        elif a > b:
            print(i + 2)
            break
