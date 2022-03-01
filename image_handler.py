#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Image handler base class."""


class ImageHandler:

    @classmethod
    def get_dimensions(cls, image):
        return image.size

    @classmethod
    def _resize_image(cls, image, size):
        width, height = image.size

        aspect_ratio = cls.calculate_aspect_ratio(image)

        if width > height:
            # Landscape
            new_width = size
            new_height = int(size * aspect_ratio)
        else:
            # Portrait
            new_height = size
            new_width = int(size * aspect_ratio)

        thumbnail = image.resize((new_width, new_height))
        return thumbnail

    @classmethod
    def calculate_aspect_ratio(cls, image):
        # Calculate aspect ratio
        width, height = image.size
        if width > height:
            # Landscape
            aspect_ratio = height / width
        else:
            # Portrait
            aspect_ratio = width / height

        return aspect_ratio

    @classmethod
    def _convert_to_grayscale(cls, image):
        image = image.convert('L')
        return image

    @classmethod
    def _get_pixels(cls, image):
        return image.load()

    @classmethod
    def prepare_image(cls, image, size):
        thumbnail = cls._resize_image(image, size)
        greyscale = cls._convert_to_grayscale(thumbnail)
        return greyscale
