#!/usr/bin/env python


from setuptools import setup, find_packages


setup(name='tikapy',
      version='2.0',
      description='Minimal Wrapper around tika jar',
      author='Felix Hummel',
      author_email='felix@felixhummel.de',
      py_modules=['tikapy'],
      install_requires=['requests'],
     )
