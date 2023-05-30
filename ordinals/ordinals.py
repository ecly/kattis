def get_ordinal(n):
    return f"{{{','.join(get_ordinal(i) for i in range(n))}}}"

print(get_ordinal(int(input())))
