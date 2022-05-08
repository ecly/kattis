import string
n = int(input())
inputs = [c == "T" for c in input().split()]
values = dict(zip(string.ascii_uppercase, inputs))
circuit = [values.get(v, v) for v in input().split()]
stack = []
while circuit:
    v = circuit.pop(0)
    if isinstance(v, bool):
        stack.append(v)
        continue

    if v in "*+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a and b if v == "*" else a or b)
    else:
        a = stack.pop()
        stack.append(not a)

print("T" if stack[0] else "F")
