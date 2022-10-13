import math
# tower in river (0) takes 1 whole day
# towers on shore or on island can be certified immediately
towers = input()
river_tower_sequences = [t for t in towers.split("1") if t]
if not river_tower_sequences:
    print(0)
else:
    longest_river_tower_sequence = max(len(t) for t in river_tower_sequences)
    print(math.ceil(longest_river_tower_sequence / 2))
