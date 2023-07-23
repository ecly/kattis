from statistics import median
n = int(input())
ks = map(int, input().split())
as_ = map(int, input().split())
ns = map(int, input().split())
for t in zip(ks,as_,ns):
    print(median(t))
