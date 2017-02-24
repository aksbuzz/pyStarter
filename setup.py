# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:

    readme = f.read()

with open('LICENSE') as f:

    license = f.read()

setup(

    name='name',

    version='0.0.1',

    description='description',

    long_description=readme,

    author='Akshay',

    author_email='akshayjr69@gmail.com',

    url='https://github.com/aksbuzz/__name__',

    license=license,

    packages=find_packages(exclude=('tests', 'docs'))
)