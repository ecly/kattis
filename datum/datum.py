d, m = [int(x) for x in input().split()]
t = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
days = d
for month in range(1, m):
    days += t[month]

dow = {
    0: "Thursday",
    1: "Friday",
    2: "Saturday",
    3: "Sunday",
    4: "Monday",
    5: "Tuesday",
    6: "Wednesday"
}
print(dow[(days-1)%7])
