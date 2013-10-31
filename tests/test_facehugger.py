#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_facehugger
----------------------------------

Tests for `facehugger` module.
"""

import os
import shutil
import tempfile
import unittest

from facehugger import facehugger


class TestFacehugger(unittest.TestCase):

    def setUp(self):
        self.output_dir = tempfile.mkdtemp()
        self.input_image = os.path.join(os.path.dirname(__file__), 'fixtures/girl-and-dog_w725_h544.jpg')

    def test_faces_in_output_dir(self):
        facehugger.main("-i {} -o {} -v".format(self.input_image, self.output_dir).split())
        self.assertEqual(len(os.listdir(self.output_dir)), 1)

    def test_faces_in_output_dir_rescaled(self):
        facehugger.main("-i {} -o {} --rescale-face-crop 20".format(self.input_image, self.output_dir).split())
        self.assertEqual(len(os.listdir(self.output_dir)), 1)

    def test_get_faces(self):
        faces = facehugger.get_faces(self.input_image, api_mode=True)
        self.assertEqual(len(faces), 1)

    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    unittest.main()
