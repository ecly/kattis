n, p, s = map(int, input().split())
for _  in range(s):
    m, *ns = list(map(int, input().split()))
    print("KEEP" if p in ns else "REMOVE")
