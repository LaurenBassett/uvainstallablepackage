#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='0.0.3',
      description='This package has shared components.',
      author='Lauren Bassett',
      author_email='laurenebassett@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
