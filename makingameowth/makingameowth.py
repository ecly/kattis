import itertools
n,p,x,y = map(int, input().split())

time = 0

for i in itertools.count(1):
    is_meowth = i % n == 0
    if p == 0:
        if is_meowth:
            time += y
        break

    if is_meowth:
        time += y
    else:
        time += x
        p -= 1


print(time)
