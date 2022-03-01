from math import floor
import os
import sys

import progressbar
from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    inverted = sys.argv[2]

    # Get original image.
    filename = sys.argv[1]
    image = ImageFileHandler.get_image(filename)

    # Shrink and convert to grayscale.
    prepared_image = ImageHandler.prepare_image(image)
    prepared_width, prepared_height = prepared_image.size
    print(f'Prepared width: {prepared_width}')

    # Blank canvas for output image.
    ascii_image = Image.new('L', image.size, (0))
    width, height = ascii_image.size

    # Calculate multiplier.
    multipler = width / prepared_width

    draw = ImageDraw.Draw(ascii_image)
    font = ImageFont.truetype('UbuntuMono.ttf', int(1.5 * multipler))

    symbols = ' _.,-=+:;cba!?0123456789$W#@Ñ'

    if inverted:
        symbols = symbols[::-1]

    pixels = ImageHandler._get_pixels(prepared_image)

    for x in progressbar.progressbar(range(0, prepared_width)):
        for y in range(0, prepared_height):
            pixel = pixels[x, y]
            symbol_index = PixelHandler.translate_pixel(
                pixel, 0, 255, 0,
                len(symbols) - 1)
            symbol = symbols[symbol_index]

            new_x = floor(x * multipler)
            new_y = floor(y * multipler)
            draw.text((new_x, new_y), symbol, font=font, fill=(255))

    ascii_image.show()
