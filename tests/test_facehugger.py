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

    def test_faces_in_output_dir(self):
        input_image = os.path.join(os.path.dirname(__file__), 'fixtures/music-166646_1280.jpg')
        facehugger.main("-i {} -o {}".format(input_image, self.output_dir).split())
        self.assertEqual(len(os.listdir(self.output_dir)), 8)

    def tearDown(self):
        shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    unittest.main()
