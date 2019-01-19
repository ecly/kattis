N = int(input())
before = input()
after = input()
switched = ''.join(map(lambda c: "0" if c == "1" else "1", before))
if N % 2 == 0 and before == after:
    print("Deletion succeeded")
elif N % 2 == 1 and after == switched:
    print("Deletion succeeded")
else:
    print("Deletion failed")
