#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as f:
    readme = f.read()



setup(
    name='hello_world_1989',  # The name of the package
    version= '0.0.1',  # the version number of the package
    description='A module to translate with country information',
    # A short description of package
    long_description=readme,
    # A long description of package
    author='Sina157',  # The maintainer
    author_email='sina.shams@yahoo.com',  # The maintainer's email address
    url='https://github.com/Sina157/translate_by_country',  # The package's website
    py_modules=['googletrans==4.0.0-rc1', ],  # The python modules to include
    license='MIT',  # The license type
    entry_points={}
)