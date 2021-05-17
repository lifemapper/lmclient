# -*- coding: utf-8 -*-
"""Package setup metadata."""
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lm_client',
    version='2.0.0',
    description='Client for accessing Lifemapper APIs',
    long_description=readme,
    author='CJ Grady',
    author_email='cjgrady@ku.edu',
    url='https://github.com/lifemapper/lm_client',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'requests']
)
