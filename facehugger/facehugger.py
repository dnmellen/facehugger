#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import argparse
from SimpleCV import Image, HaarCascade

from utils import scale_bounding_box

# HaarCascade to segment faces
segment_face = HaarCascade(os.path.join(os.path.abspath(os.path.dirname(__file__)), "haarcascade_frontalface_alt2.xml"))


def get_faces(image_path, api_mode=False, rescale_face_crop=0):
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
        if rescale_face_crop:
            return [original_image.crop(scale_bounding_box(face.boundingBox(), rescale_face_crop)) for face in faces]
        else:
            return [face.crop() for face in faces]


def main(args=None):
    """
    Execution as command
    """

    parser = argparse.ArgumentParser(description='Extracts faces from an image')
    parser.add_argument('-i', '--image-path', help='Image path', required=True)
    parser.add_argument('-o', '--output-dir', help='Output directory', required=True)
    parser.add_argument('--rescale-face-crop', help='Augment face crop in percentage', type=int, required=False, default=0)
    parser.add_argument('-v', '--verbose', help='Verbose', required=False, action='store_true')
    options = vars(parser.parse_args(args))

    faces = get_faces(options['image_path'], rescale_face_crop=options['rescale_face_crop'])

    if options['verbose']:
        print("Found {} faces on {}".format(len(faces), options['image_path']))
    for n, face in enumerate(faces):
        face.save(os.path.join(options['output_dir'], 'face_{}.jpg'.format(n)))

if __name__ == '__main__':  # pragma: no cover
    main()
