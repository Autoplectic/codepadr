# encoding: utf-8
from setuptools import setup

setup(
    name='codepadr',
    version='1.0',
    url="https://github.com/autoplectic/codepadr",
    license="LITL",
    description="A tool for uploading to codepad.org",
    author="Ryan James",
    author_email="rgjames@ucdavis.edu",
    packages=['codepadr'],
    install_requires=['argparse', 'requests'],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points={'console_scripts': ['codepad = codepadr.cli:main']}
)

