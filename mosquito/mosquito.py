import fileinput
for line in fileinput.input():
    M, P, L, E, R, S, N = map(int, line.split())
    pupae = P
    larvae = L
    mosquitoes = M
    for _ in range(N):
        eggs = mosquitoes * E
        mosquitoes = pupae // S
        pupae = larvae // R
        larvae = eggs

    print(mosquitoes)
