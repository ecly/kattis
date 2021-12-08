smiles = input()
valid_smiles = [":)", ";)", ":-)", ";-)"]
indexes = []
for i in range(len(smiles)):
    s = smiles[i:]
    if any(s.startswith(smile) for smile in valid_smiles):
        indexes.append(i)

print("\n".join(map(str, indexes)))
