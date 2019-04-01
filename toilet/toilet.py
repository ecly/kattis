input_ = input()

pol1 = input_[1:].count("D") * 2
if input_[0] == "D" and input_[1] == "D":
    pol1 -= 1
elif input_[0] == "D" and input_[1] == "U":
    pol1 += 1

pol2 = input_[1:].count("U") * 2
if input_[0] == "U" and input_[1] == "U":
    pol2 -= 1
elif input_[0] == "U" and input_[1] == "D":
    pol2 += 1

pol3 = len(list(filter(lambda l: l[0] != l[1], zip(input_, input_[1:]))))

print(pol1)
print(pol2)
print(pol3)
