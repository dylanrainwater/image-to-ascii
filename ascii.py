from PIL import Image
import numpy as np
import sys

ASCII_GRADIENT = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
size = (140, 140)

def getBrightness(p):
    # lightness = int((max(pixel) + min(pixel)) / 3)
    # luminosity = int((0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2]) / 3)
    avg = int(sum(pixel) / 3)
    return avg

def brightnessToAscii(brightness, maxBrightness=255):
    index = int((brightness / maxBrightness) * (len(ASCII_GRADIENT) - 1))
    return ASCII_GRADIENT[index]    

if __name__ == "__main__":
    im = Image.open("input.jpg")
    im.thumbnail(size, Image.ANTIALIAS)

    # Get RGB matrix
    rgb_vals = np.asarray(im)

    for x in range(len(rgb_vals)):
        for y in range(len(rgb_vals[0])):
            pixel = rgb_vals[x][y]
            brightness = getBrightness(pixel)
            ascii_val = brightnessToAscii(brightness)
            print(ascii_val * 2, end="")
        print()