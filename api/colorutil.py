def hsv_to_hex(h, s, v): # Used for rainbow
    h = float(h)
    s = float(s) / 100
    v = float(v) / 100

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60: r, g, b = c, x, 0
    elif 60 <= h < 120: r, g, b = x, c, 0
    elif 120 <= h < 180: r, g, b = 0, c, x
    elif 180 <= h < 240: r, g, b = 0, x, c
    elif 240 <= h < 300: r, g, b = x, 0, c
    elif 300 <= h < 360: r, g, b = c, 0, x
    else: r, g, b = 0, 0, 0

    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return f'#{r:02x}{g:02x}{b:02x}'

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])