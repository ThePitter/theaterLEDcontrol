import math


wavecount = 10
color_a = (255, 255, 255)
color_b = (0, 0, 0)
speed = math.pi * 0.02



pos = 0.0
def play(strip):
    stripcount = len(strip)
    pixels_per_wave = stripcount / wavecount
    rotaion_per_pixel = (math.pi * 2) / pixels_per_wave

    shift = pos
    for pixel in strip:
        value = math.sin(shift)
        pixel = (mid(value, -1, 1, color_a[0], color_b[0]), mid(value, -1, 1, color_a[1], color_b[1]), mid(value, -1, 1, color_a[2], color_b[2]))
        shift += rotaion_per_pixel
    pos += speed
    if pos >= math.pi * 2:
        pos -= math.pi * 2

    return

def mid(value, low, high, outlow, outhigh):
    value -= low
    high -= low
    low = 0
    ratio = value / high
    tempout = (outhigh - outlow) * ratio
    return tempout + outlow