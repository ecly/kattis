notes = "A,A#,B,C,C#,D,D#,E,F,F#,G,G#".split(",")
scale_definition = [2, 2, 1, 2, 2, 2, 1]
scales = []
for i, c in enumerate(notes):
    scale = [c]
    pointer = i
    for j in scale_definition:
        pointer += j
        scale.append(notes[pointer % len(notes)])

    scales.append(scale)

_n = input()
played = set(input().split())
usable_scales = []
for scale in scales:
    if all(note in scale for note in played):
        usable_scales.append(scale[0])

if usable_scales:
    print(" ".join(sorted(usable_scales)))
else:
    print("none")
