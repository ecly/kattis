action, string = input().split()
if action == "D":
    res = ""
    for i in range(0, len(string), 2):
        c = string[i]
        count = int(string[i+1])
        res += c * count
    print(res)
else:
    res = ""
    current = ""
    count = 0
    for c in string:
        if c == current:
            count += 1
        else:
            if current:
                res += "%s%d" % (current, count)

            current = c
            count = 1

    res += "%s%d" % (current, count)
    print(res)
