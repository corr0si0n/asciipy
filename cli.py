#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI to convert images to ASCII."""

import click

from ascii_handler import ASCIIHandler


@click.group()
def cli():
    pass


@cli.command()
@click.option('--size', default=64, help='Output file size in pixels.')
@click.option('--inverted', default=False, help='Invert the output image.')
@click.argument('infile')
def ascii(infile, size, inverted):
    ASCIIHandler.asciify(infile, inverted, size)


if __name__ == '__main__':
    cli()
