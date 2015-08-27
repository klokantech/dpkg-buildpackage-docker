#!/usr/bin/env python

from setuptools import setup

entry_points = """
[console_scripts]
dpkg-buildpackage-docker=dpkg_buildpackage:main
"""

setup(
    name='dpkg-buildpackage',
    version='0.0.1',
    description='Klokantech dpkg-buildpackage for Docker',
    py_modules=['dpkg_buildpackage'],
    entry_points=entry_points)
