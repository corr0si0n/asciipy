#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ASCII handler base class."""
from PIL import Image, ImageDraw, ImageFont

from image_file_handler import ImageFileHandler
from image_handler import ImageHandler
from pixel_handler import PixelHandler


class ASCIIHandler:

    @classmethod
    def asciify(cls, filename, inverted, size):
        """Convert an image to ascii art."""
        print('Converting image to ASCII...')

        image = ImageFileHandler.get_image(filename)

        prepared_image = ImageHandler.prepare_image(image, size)
        prepared_width, prepared_height = prepared_image.size

        # Blank canvas for output image.
        ascii_image = Image.new('L', image.size, (0))
        width, _ = ascii_image.size

        # Calculate multiplier.
        multiplier = width / prepared_width

        draw = ImageDraw.Draw(ascii_image)
        font = ImageFont.truetype('UbuntuMono.ttf', int(1.5 * multiplier))

        symbols = ' _.,-=+:;cba!?0123456789$W#@Ñ'

        if inverted:
            symbols = symbols[::-1]

        pixels = ImageHandler._get_pixels(prepared_image)

        for x in (range(0, prepared_width)):
            for y in range(0, prepared_height):
                pixel = pixels[x, y]
                symbol_index = PixelHandler.translate_pixel(
                    pixel, 0, 255, 0,
                    len(symbols) - 1)
                symbol = symbols[symbol_index]

                new_x = round(x * multiplier)
                new_y = round(y * multiplier)
                draw.text((new_x, new_y), symbol, font=font, fill=(pixel))

        ascii_image.show()

        print('Done')
