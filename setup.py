#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
version = __import__('facehugger').__version__

setup(
    name='facehugger',
    version=version,
    description='Extracts faces from an image',
    long_description=readme + '\n\n' + history,
    author='Diego Navarro Mellen',
    author_email='dnmellen@gmail.com',
    url='https://github.com/dnmellen/facehugger',
    packages=[
        'facehugger',
    ],
    package_dir={'facehugger': 'facehugger'},
    include_package_data=True,
    install_requires=[
        'SimpleCV',
    ],
    license="BSD",
    zip_safe=False,
    keywords=['facehugger', 'simplecv', 'vision', 'face', 'crawl'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Utilities',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'facehugger = facehugger.facehugger:main',
        ]
    }
)
