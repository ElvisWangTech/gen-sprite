#! encoding:UTF-8
from wand.image import Image

"""
convert by wand
"""


def convert_wand(input_path, output_path, export_type="PNG"):
    img=Image(input_path)
    img.convert(export_type)
    img.save(filename=output_path)


