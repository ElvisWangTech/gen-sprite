#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir,path
from PIL import Image
from config import ConfigReader

output_path = '.'

im_ex = '.png'

o_im_ex = '.png'

ims = []

max_size = None

page_size = 2

row = None

col = None

flow = 0

svg_lib = None

# belows used inner
im_mode = None

width = None

height = None


# jpg has max size limit.
def check_valid_size():
    pass


def save_part(page_index, page_size):

    print('page_index:{0}, page_size:{1}, flow: {2}'.format(page_index, page_size, flow))

    _width = width * (page_size if flow == 0 else 1)

    _height = height * (page_size if flow == 1 else 1)

    result = Image.new(im_mode, (_width, _height))

    for i, im in enumerate(ims[page_index * page_size:page_index * page_size + page_size]):

        if flow == 1:  # vertical attend

            result.paste(im, box=(0, i * height))

        else:

            result.paste(im, box=(i * width, 0))

    save_path = path.join(output_path, 'img{0}{1}'.format(page_index, o_im_ex))

    print("saving part image %s" % save_path)

    result.save(save_path)


def init():

    print("reading config...")

    global output_path, im_ex, o_im_ex, ims, max_size, page_size, row, col, svg_lib, flow

    config_reader = ConfigReader.get_main_config()

    path = config_reader.get("path", "input_dir")

    output_path = config_reader.get("path", "output_dir")

    im_ex = config_reader.get("param", "ext")

    o_im_ex = config_reader.get("param", "out_ext")

    page_size = int(config_reader.get("param", "page_size"))

    dirs = listdir(path)

    ims = [Image.open(('%s%s' % (path, fn))) for fn in sorted(dirs) if fn.endswith(im_ex)]

    max_size = len(ims)

    row = config_reader.get("param", "row")

    col = config_reader.get("param", "col")

    flow = int(config_reader.get("param", "flow"))

    svg_lib = config_reader.get("param", "svg_lib")

    print("initialized")


def main():

    init()

    global im_mode, width, height

    if max_size > 0:

        page_index = 0

        im_mode = ims[0].mode

        width, height = ims[0].size

        while (page_index + 1) * page_size <= max_size:

            save_part(page_index, page_size)

            page_index += 1

        left_size = max_size - page_index * page_size

        if left_size > 0:

            save_part(page_index, left_size)

    else:

        print('no file')


if __name__ == '__main__':
    main()
