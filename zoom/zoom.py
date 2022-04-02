_n, k = map(int, input().split())
ns = list(map(int, input().split()))
print(*ns[k-1::k])
