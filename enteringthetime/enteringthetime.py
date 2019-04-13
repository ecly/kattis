source = list(input().replace(":", ""))
target = list(input().replace(":", ""))
source = list(map(int, source))
target = list(map(int, target))

def format(t):
    return str(t[0]) + str(t[1]) + ":" + str(t[2]) + str(t[3])

steps = [format(source)]
order = [3,2,1,0] if target[0] == 2 else [3,2,0,1]
while source != target:
    for i in order:
        if source[i] != target[i]:
            if i == 2:
                if target[i] < source[i]:
                    source[i] -= 1
                else:
                    source[i] += 1
            elif i == 1 and source[0] == 2:
                if target[i] < source[i]:
                    source[i] -= 1
                else:
                    source[i] += 1
            elif target[i] > source[i] and target[i] - source[i] > 5:
                source[i] -= 1
            elif target[i] > source[i]:
                source[i] += 1
            elif target[i] < source[i] and source[i] - target[i] > 5:
                source[i] += 1
            else:
                source[i] -= 1

            if source[i] < 0:
                source[i] = 9
            if source[i] > 9:
                source[i] = 0
            break

    steps.append(format(source))

print(len(steps))
print("\n".join(steps))
