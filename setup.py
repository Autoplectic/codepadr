#!/usr/bin/env python
# encoding: utf-8

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='codepadr',
    version='0.9',
    description="A tool for uploading to codepad.org",
    long_description=read('README.rst'),
    author="Ryan James",
    author_email="rgjames@ucdavis.edu",
    url="https://github.com/autoplectic/codepadr",
    license="LITL",
    packages=['codepadr'],
    install_requires=['argparse', 'requests'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points={'console_scripts': ['codepad = codepadr.cli:main']}
)

