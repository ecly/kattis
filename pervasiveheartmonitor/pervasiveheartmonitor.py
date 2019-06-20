import fileinput
from statistics import mean
for line in fileinput.input():
    words = line.split()
    name = " ".join(w for w in words if w.isalpha())
    rates = [float(w) for w in words if not w.isalpha()]
    print(f"{mean(rates)} {name}")
