import fileinput
morse = {
    "A": ".-",
    "H": "....",
    "O": "---",
    "V": "...-",
    "B": "-...",
    "I": "..",
    "P": ".--.",
    "W": ".--",
    "C": "-.-.",
    "J": ".---",
    "Q": "--.-",
    "X": "-..-",
    "D": "-..",
    "K": "-.-",
    "R": ".-.",
    "Y": "-.--",
    "E": ".",
    "L": ".-..",
    "S": "...",
    "Z": "--..",
    "F": "..-.",
    "M": "--",
    "T": "-",
    "G": "--.",
    "N": "-.",
    "U": "..-",
    "_": "..--",
    ",": ".-.-",
    ".": "---.",
    "?": "----"
}
morse_rev = {v: k for k, v in morse.items()}

for line in fileinput.input():
    lens = []
    code = ""
    for c in line.strip():
        code += morse[c]
        lens.append(len(morse[c]))

    ptr = 0
    msg = ""
    for l in lens[::-1]:
        msg += morse_rev[code[ptr:ptr+l]]
        ptr += l

    print(msg)
