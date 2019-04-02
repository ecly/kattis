import itertools
m = int(input())
add = "+ 4"
sub = "- 4"
mul = "* 4"
div = "// 4"
permutations = list(itertools.product([add, sub, mul, div], repeat=3))

def eval_perm(perm):
    return eval("".join(("4",) + perm))

def pprint_perm(perm, n):
    return " ".join(("4",) + perm + ("= %d" % n,)).replace("//", "/")

for _ in range(m):
    n = int(input())
    res = None
    for perm in permutations:
        if eval_perm(perm) == n:
            res = pprint_perm(perm, n)
            break

    print(res if res is not None else "no solution")
