from datetime import datetime

current_time = datetime.strptime(input(), "%H:%M:%S")
explosion_time = datetime.strptime(input(), "%H:%M:%S")

delta = explosion_time - current_time
delta_seconds = delta.total_seconds()
if delta_seconds < 0:
    delta_seconds = delta_seconds + 60 * 60 * 24

if delta_seconds == 0:
    print("24:00:00")
else:
    hours, rem = divmod(delta_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

