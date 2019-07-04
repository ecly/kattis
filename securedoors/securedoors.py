n = int(input())
inside = set()
for _ in range(n):
    action, entity = input().split()
    out = [entity]
    if action == "entry":
        out.append("entered")
        if entity in inside:
            out.append("(ANOMALY)")

        inside.add(entity)

    if action == "exit":
        out.append("exited")
        if entity not in inside:
            out.append("(ANOMALY)")
        else:
            inside.remove(entity)

    print(" ".join(out))
