p, q = map(int, input().split())
positions = input()
l = list(range(1, p))
m = list(range(p+1,q))
h = list(range(q+1,10))
if positions == "ABBA" and len(m) == 2:
    print(*m)
elif positions == "BBAA" and len(l) == 2:
    print(*l)
elif positions == "AABB" and len(h) == 2:
    print(*h)
elif positions == "BABA" and len(l) == 1 and len(m) == 1:
    print(*(l + m))
elif positions == "ABAB" and len(m) == 1 and len(h) == 1:
    print(*(m + h))
elif positions == "BAAB" and len(l) == 1 and len(h) == 1:
    print(*(l + h))
else:
    print(-1)
