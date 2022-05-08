#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import getopt

"""
This is a tool to convert svg files to jpg or png.
"""


def convert(_from_dir, target_dir=".", _export_type="JPG", mod="wand"):
    print("scan svg files in " + _from_dir)

    # check if target directory exist
    if not os.path.exists(target_dir):

        os.makedirs(target_dir)

    num = 0

    for a, f, c in os.walk(_from_dir):

        for file_name in c:

            path = os.path.join(a, file_name)

            if os.path.isfile(path) and file_name[-3:] == "svg":

                num += 1

                export_path = os.path.join(target_dir, file_name[:-3] + _export_type.lower())

                try:

                    if mod == "wand":

                        _mod = __import__("_wand")

                        _mod.convert_wand(path, export_path, _export_type)

                    elif mod == "svglib":

                        _mod = __import__("_svglib")

                        _mod.convert_svglib(path, export_path, _export_type)

                except:

                    print("error in convert svg file: %s to %s" % (path, _export_type))


def usage():

    print('\n{0} Usage:'.format(sys.argv[0]))

    print('options: from_dir target_dir [export_type=JPG]')

    print('eg: {0} svg_dir export_dir PNG'.format(sys.argv[0]))


def main():
    try:

        opts, args = getopt.getopt(sys.argv[1:], "i:ho:t:m:", ["help", "output=", "input=", "mod="])

        inputs = args[0]

    except getopt.GetoptError as err:

        print(err)

        usage()

        sys.exit(2)

    output = '.'

    export_type = 'JPG'

    mod = 'svglib'

    print(opts)

    for o, a in opts:

        if o in ("-h", "--help"):

            usage()

            sys.exit()

        elif o in ("-o", "--output"):

            output = a

        elif o in ("-i", "--input"):

            inputs = a

        elif o in ("-t", "--type"):

            export_type = a

        elif o in ("-m", "--mod"):

            mod = a

        else:

            assert False, "unhandled option"

    convert(inputs, output, export_type.upper(), mod)


if __name__ == '__main__':

    main()

