import sys
t = int(sys.stdin.readline())
sys.stdin.readline()
for _ in range(t):
    candies = 0
    n = int(sys.stdin.readline())
    while True:
        i = sys.stdin.readline().strip()
        if not i:
            break

        candies += int(i)

    print("YES" if  candies % n == 0 else "NO")
