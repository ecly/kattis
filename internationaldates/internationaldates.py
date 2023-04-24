a, b, _ = map(int, input().split("/"))
print("EU" if a > 12 else "US" if b > 12 else "either")
