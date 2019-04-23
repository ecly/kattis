T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    if K > 0 and (K + 1) % 2**N == 0:
        print("Case #%d: ON" % case)
    else:
        print("Case #%d: OFF" % case)
