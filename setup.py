#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import codecs
import os
import sys

from setuptools import find_packages, setup


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


def local_read(name):
    return codecs.open(name).read()


SOURCE = local_file('src')
README = local_read('README.rst')
HISTORY = local_read('HISTORY.rst')
long_description = u'\n\n'.join([README, HISTORY])


# Stealing this from Kenneth Reitz
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='specktre',
    version='0.1.0',
    description='A tool for creating wallpapers with Python',
    long_description=long_description,
    url='https://github.com/alexwlchan/specktre',
    author='Alex Chan',
    author_email='alex@alexwlchan.net',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production / Stable',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='images wallpaper',
    packages=find_packages(SOURCE),
    package_data={'': ['LICENSE', 'README.rst', 'HISTORY.rst']},
    package_dir={'': SOURCE},
    include_package_data=True,
    install_requires=[
        'docopt',
        'Pillow',
    ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'specktre=specktre:main',
        ],
    },
)