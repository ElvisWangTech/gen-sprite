#! encoding:UTF-8
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

"""
convert by svglib
"""


def convert_svglib(input_path, output_path, export_type="PNG"):
    drawing = svg2rlg(input_path)

    renderPM.drawToFile(drawing, output_path, fmt=export_type)


