def rotate(l, rot):
    return [(x + rot) % 26 for x in l]

ascii_offset = 65
drm = [ord(c) - ascii_offset for c in input()]
middle = len(drm) // 2
l, r = drm[:middle], drm[middle:]
lr, rr = rotate(l, sum(l)), rotate(r, sum(r))
print(''.join([chr(ascii_offset + (x+y) % 26) for x,y in zip(lr, rr)]))
