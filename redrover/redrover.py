route = input()
best = len(route)
for sz in range(1, len(route) // 3 + 1):
    for i in range(len(route) - sz):
        macro = route[i:i+sz]
        score = len(route.replace(macro, "M")) + len(macro)
        if score < best:
            best = score

print(best)
