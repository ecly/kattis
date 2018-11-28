from collections import Counter
xa = []
ya = []
for _ in range(3):
    x, y = input().split()
    xa.append(int(x))
    ya.append(int(y))

xm = next(k for k,v in Counter(xa).items() if v==1)
ym = next(k for k,v in Counter(ya).items() if v==1)
print(xm, ym)
