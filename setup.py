# -*- coding: utf-8 -*-
"""Package setup metadata."""
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lmclient',
    version='2.0.0b2',
    description='Client for accessing Lifemapper APIs',
    long_description=readme,
    author='CJ Grady',
    author_email='cjgrady@ku.edu',
    url='https://github.com/lifemapper/lmclient',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'requests'
    ]
)
