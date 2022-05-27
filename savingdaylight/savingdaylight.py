import sys
from datetime import datetime

lines = sys.stdin.read().strip().split("\n")
for line in lines:
    fields = line.strip().split()
    sunrise, sunset = map(lambda d: "0" + d if len(d) == 4 else d, fields[-2:])
    sunrise, sunset = map(lambda d: datetime.strptime(d, "%H:%M"), [sunrise, sunset])
    delta = sunset - sunrise
    delta_seconds = delta.total_seconds()
    hours, rem = divmod(delta_seconds, 3600)
    minutes = rem // 60
    print(*fields[:-2], int(hours), "hours", int(minutes), "minutes")
