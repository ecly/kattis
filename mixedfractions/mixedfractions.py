import sys
for line in sys.stdin.readlines()[:-1]:
    num, dem = list(map(int, line.split()))
    whole = num // dem
    proper_num = num % dem
    print("%d %d / %d" % (whole, proper_num, dem))
