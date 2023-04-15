deduped = []
for c in input():
    if not deduped or c != deduped[-1]:
        deduped.append(c)
print("".join(deduped))
