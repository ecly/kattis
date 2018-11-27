import sys
for l in sys.stdin.readlines()[1:]:
    k, n = [int(x) for x in l.split()]
    s1 = sum(range(n+1))
    s2 = sum(range(1,n*2+1,2))
    s3 = sum(range(2,n*2+1,2))
    print(k, s1, s2, s3)
