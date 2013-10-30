#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import argparse
from SimpleCV import Image, HaarCascade

# HaarCascade to segment faces
segment_face = HaarCascade(os.path.join(os.path.dirname(__file__), "haarcascade_frontalface_alt.xml"))


def get_faces(image_path, api_mode=False):
    """
    Return a list of cropped faces given an image path

    :param image_path: Path to image
    :type image_path: str
    :param api_mode: If api_mode is True get_faces returns a list of found HaarFeatures
    :type api_mode: bool
    :returns: list of images
    """

    original_image = Image(image_path)
    faces = original_image.findHaarFeatures(segment_face)

    if api_mode:
        return faces
    else:
        return [face.crop() for face in faces]


def main(args=None):
    """
    Execution as command
    """

    parser = argparse.ArgumentParser(description='Extracts faces from an image')
    parser.add_argument('-i', '--image-path', help='Image path', required=True)
    parser.add_argument('-o', '--output-dir', help='Output directory', required=True)
    parser.add_argument('-v', '--verbose', help='Verbose', required=False, action='store_true')
    options = vars(parser.parse_args(args))

    faces = get_faces(options['image_path'])

    if options['verbose']:
        print("Found {} faces on {}".format(len(faces), options['image_path']))
    for n, face in enumerate(faces):
        face.save(os.path.join(options['output_dir'], 'face_{}.jpg'.format(n)))

if __name__ == '__main__':
    main()
