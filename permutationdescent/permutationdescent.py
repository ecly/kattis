from functools import lru_cache

MOD = 1001113

@lru_cache()
def perms(n, v):
    if v in (0, n - 1):
        return 1

    return (v + 1) * perms(n - 1, v) + (n - v) * perms(n - 1, v - 1)

def main():
    P = int(input())
    for _ in range(P):
        K, N, v = map(int, input().split())
        pdc = perms(N, v)
        result = pdc % MOD
        print(K, result)

if __name__ == '__main__':
    main()
