def find_smaller(number):
    n_sum = sum(int(x) for x in str(number))
    for i in range(number - 1, 0, -1):
        i_sum = sum(int(x) for x in str(i))
        if n_sum - i_sum == 1:
            return i

    return 0


for _ in range(int(input())):
    n = int(input())
    print(find_smaller(n))
