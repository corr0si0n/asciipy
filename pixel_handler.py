#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pixel handler base class."""


class PixelHandler:

    @classmethod
    def translate_pixel(cls, value, min, max, new_min, new_max):
        old_range = max - min
        new_range = new_max - new_min
        return int(((value - min) * new_range) / old_range + new_min)
