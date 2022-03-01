#!/usr/bin/env pythno3
# -*- coding: utf-8 -*-
"""Image file handler base class."""

import os

from PIL import Image


class ImageFileHandler:

    @classmethod
    def get_image(cls, filename):
        if os.path.isdir(filename):
            raise ValueError(f'{filename} is a directory.')
        elif os.path.exists(filename):
            filepath = filename
        else:
            cwd = os.getcwd()
            filepath = f'{cwd}/{filename}'

        # Fetch and return the image.
        return Image.open(filepath)
